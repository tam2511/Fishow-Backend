export default function ({ $axios, redirect }) {
  // Django CSRF configuration
  $axios.onRequest((config, userEntity) => {
    config.xsrfCookieName = 'csrftoken'
    config.xsrfHeaderName = 'X-CSRFToken'
  })
  // $axios.onResponse((response) => {
  // })
}
