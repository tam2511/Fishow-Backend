import axios from 'axios'
import confserver from '~/confserver'

const apiClient = axios.create({
  baseURL: confserver.ip,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
  },
})

export default {
  getUserData() {
    return apiClient.get('/dj-rest-auth/user/')
  },
  getAllUsers() {
    return apiClient.get('/user_all/')
  },
}
