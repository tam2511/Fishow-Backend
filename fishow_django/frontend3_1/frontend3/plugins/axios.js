export default function ({ $axios, redirect }) {
  // Django CSRF configuration
  $axios.onRequest((config, userEntity) => {
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'x-csrftoken'
  })
  $axios.onResponse((response) => {
    // if (response.data.key) {
    //   // document.cookie = 'sessionid=' + response.data.key
    // }
  })
  $axios.onError((error) => {
    if (error.response.status === 500) {
      redirect('/sorry')
    }
  })
}
