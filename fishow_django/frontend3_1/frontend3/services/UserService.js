import axios from 'axios'
import confserver from '~/confserver'

const apiClient = axios.create({
  baseURL: `http://${confserver.ip}:8000/api`,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
  },
})

export default {
  getUserData() {
    return apiClient.get('/rest-auth/user/')
  },
  getAllUsers() {
    return apiClient.get('/user_all/')
  },
}
