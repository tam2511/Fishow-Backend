export default function ({ $axios, redirect }) {
  // Django CSRF configuration
  $axios.onRequest((config, userEntity) => {
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
  })
  $axios.onResponse((response) => {
    if (response.data.key) {
      document.cookie = 'sessionid=' + response.data.key
    }
  })
  $axios.onError((error) => {
    console.log('error axios = ', error)
    // const code = parseInt(error.response && error.response.status)
    // if (code === 400) {
    //   redirect('/400')
    // }
  })
}
