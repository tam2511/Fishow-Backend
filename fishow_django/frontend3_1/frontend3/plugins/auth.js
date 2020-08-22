export default function ({ $auth }) {
  // eslint-disable-next-line handle-callback-err
  $auth.onError((error, name, endpoint) => {
    // console.error(name, error)
  })
}
