export default function ({ $axios, redirect }) {
  // Django CSRF configuration
  $axios.onRequest((config, userEntity) => {
    console.log('config = ', config)
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
  })
  $axios.onResponse((response) => {
    console.log('response 2 = ', response)
    if (response.data.key) {
      $axios.setHeader('Authorization', 'Token ' + response.data.key)
    }
  })
  $axios.onError((error) => {
    const code = parseInt(error.response && error.response.status)
    if (code === 400) {
      redirect('/400')
    }
  })
}
