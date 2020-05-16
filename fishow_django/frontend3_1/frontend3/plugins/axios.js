export default function ({ $axios, redirect }) {
  // Django CSRF configuration
  $axios.onRequest((config, userEntity) => {
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
  })
  $axios.onResponse((response) => {
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
