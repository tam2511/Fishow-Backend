import axios from 'axios'
import { NotificationProgrammatic as Notification } from 'buefy'

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
  async getBlogComment(slug) {
    Notification.open('Notify!')

    return await apiClient.get(`/blogs/${slug}/comments/`)
  },
  async postBlogComment(slug, data) {
    return await apiClient.post(`/blogs/${slug}/comments/`, data)
  },
}
