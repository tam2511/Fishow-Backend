const strategy = 'local'
const FALLBACK_INTERVAL = 900 * 1000 * 0.75

async function refreshTokenF($auth, $axios, token, refreshToken) {
  if (token && refreshToken) {
    try {
      const response = await $axios.post('/dj-rest-auth/token/refresh/', {
        refresh: refreshToken,
      })
      token = 'Bearer ' + response.data.access_token
      // console.log('refresh token = ', token)
      refreshToken = response.data.refresh_token

      $auth.setToken(strategy, token)
      $auth.setRefreshToken(strategy, refreshToken)
      $axios.setToken(token)
      return decodeToken.call(this, token).exp
    } catch (error) {
      $auth.logout()
      throw new Error('Error while refreshing token')
    }
  }
}

export default async function ({ app }) {
  const { $axios, $auth } = app

  let token = $auth.getToken(strategy)
  // console.log('token = ', token)
  let refreshToken = $auth.getRefreshToken(strategy)
  // console.log('refreshToken = ', refreshToken)
  let refreshInterval = FALLBACK_INTERVAL
  if (token && refreshToken) {
    $axios.get('/dj-rest-auth/user/').then((resp) => {
      // console.log('resp.data = ', resp.data)
      $auth.setUser(resp.data)
    })
    const tokenParsed = decodeToken.call(this, token)
    refreshInterval = (tokenParsed.exp * 1000 - Date.now()) * 0.75

    if (refreshInterval < 10000 && refreshInterval > 0) {
      refreshInterval = 10000
    }
    if (refreshInterval < 0) {
      refreshInterval =
        ((await refreshTokenF($auth, $axios, token, refreshToken)) * 1000 -
          Date.now()) *
        0.75
      $auth.fetchUserOnce()
    }
  }
  setInterval(async function () {
    token = $auth.getToken(strategy)
    refreshToken = $auth.getRefreshToken(strategy)
    await refreshTokenF($auth, $axios, token, refreshToken)
  }, refreshInterval)
}
function decodeToken(str) {
  // console.log('decode input ', str)
  str = str.split('.')[1]

  str = str.replace('/-/g', '+')
  str = str.replace('/_/g', '/')
  switch (str.length % 4) {
    case 0:
      break
    case 2:
      str += '=='
      break
    case 3:
      str += '='
      break
    default:
      throw new Error('Invalid token')
  }

  str = (str + '===').slice(0, str.length + (str.length % 4))
  str = str.replace(/-/g, '+').replace(/_/g, '/')

  str = decodeURIComponent(
    escape(Buffer.from(str, 'base64').toString('binary'))
  )

  str = JSON.parse(str)
  // console.log('decode result = ', str)
  return str
}
