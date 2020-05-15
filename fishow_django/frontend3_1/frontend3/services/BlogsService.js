import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
  },
})

export default {
  getBlogs() {
    return apiClient.get('/blogs/')
  },
  getBlog(slug) {
    return apiClient.get(`/blogs/${slug}/`)
  },
}
