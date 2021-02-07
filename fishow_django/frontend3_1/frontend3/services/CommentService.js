import axios from 'axios'
import confserver from '~/confserver'

const apiClient = axios.create({
  baseURL: `https://${confserver.ip}/api`,
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
  },
})

export default {
  getBlogComment(slug) {
    return apiClient.get(`/blogs/${slug}/comments/`)
  },
  postBlogComment(slug, data) {
    return apiClient.post(`/blogs/${slug}/comments/`, data)
  },
}
