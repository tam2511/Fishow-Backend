export default function ({ $axios, redirect }) {
  // Django CSRF configuration
  $axios.onRequest((config, userEntity) => {
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
    console.log('config = ', config)
  })
  $axios.onResponse((response) => {
    if (response.data) {
      console.log('response.data = ', response.data)
      // document.cookie = 'sessionid=' + response.data.key
    }
  })
  // $axios.onError((error) => {
  //   if (error.response.status === 500) {
  //     // redirect('/sorry')
  //   }
  // })
}
