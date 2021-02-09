import axios from 'axios'
import dev from '~/confserver'
const API = dev.ip
export default {
  getHeaders() {
    return {
      headers: {
        Authorization: `${localStorage.getItem('auth._token.local')}`,
      },
    }
  },
  get(url) {
    return axios.get(url, this.getHeaders())
  },
  postLogin(url, data) {
    return axios.post(url, data)
  },
  post(url, data) {
    return axios.post(url, data, this.getHeaders())
  },
  put(url, data) {
    return axios.put(url, data, this.getHeaders())
  },
  delete(url) {
    return axios.delete(url, this.getHeaders())
  },
  login(data) {
    return this.postLogin(`${API}/dj-rest-auth/login/`, data)
  },
  registration(data) {
    return this.post(`${API}/registration`, data)
  },
  getUser() {
    return this.get(`${API}/dj-rest-auth/user/`)
  },
  getRegions(params = '') {
    return this.get(`${API}/region/${params}`)
  },
  getWaterPlacesNature(params = '') {
    return this.get(`${API}/waterplace_nature/${params}`)
  },
}
