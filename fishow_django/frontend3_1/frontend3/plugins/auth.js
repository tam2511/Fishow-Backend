const strategy = 'local'

export default async function ({ app }) {
  const { $axios, $auth } = app
  const token = $auth.getToken(strategy)
  const refreshToken = $auth.getRefreshToken(strategy)
  if (token && refreshToken) {
    $axios.get('/dj-rest-auth/user/').then((resp) => {
      $auth.setUser(resp.data)
    })
    const refreshInterval = decodeToken.call(this, token).exp
    const timeLeft = (refreshInterval * 1000 - Date.now()) * 0.75
    if (timeLeft < 5) {
      try {
        const response = await $axios.post('/dj-rest-auth/token/refresh/', {
          refresh: refreshToken,
        })
        const token = 'Bearer ' + response.data.access
        $auth.setToken(strategy, token)
      } catch (e) {
        $auth.logout()
        console.error(e)
      }
    }
  }
}
function decodeToken(str) {
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
  return str
}
