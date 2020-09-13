import axios from 'axios'
import confserver from '~/confserver'

let token = null

if (process.client) {
  const step1 = document.cookie.split('auth._token.local=')
  const step2 = step1[1].split(';')
  token = decodeURI(step2[0])
}
const apiClient = axios.create({
  baseURL: `http://${confserver.ip}:8000/api`,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
    Authorization: token,
  },
})

export default {
  getBlogs() {
    return apiClient.get('/blogs/')
  },
  getBlog(slug) {
    return apiClient.get(`/blogs/${slug}/`)
  },
  postBlog(data) {
    return apiClient.post('/blogs/', data)
  },
}
// Authorization:
// 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMDEyMjg5LCJqdGkiOiI0YWI5NDY1OTRkYzc0NWViYWMzMWRjZTE0ZWYwY2FjNSIsInVzZXJfaWQiOjl9.oq5jL-GCBxfV5GurJeLud953bEoIMXAsVvV_r99KXnE',
