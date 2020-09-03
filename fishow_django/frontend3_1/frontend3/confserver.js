const os = require('os')

const server = {
  ip: '213.139.208.107',
}
const dev = {
  ip: '127.0.0.1',
}

const current =
  !process.browser && os.userInfo() && os.userInfo().username === 'root'
    ? server
    : dev

export default current
