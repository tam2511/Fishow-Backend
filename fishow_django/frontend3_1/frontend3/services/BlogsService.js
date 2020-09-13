// import axios from 'axios'
// import confserver from '~/confserver'

// const apiClient = axios.create({
//   baseURL: `http://${confserver.ip}:8000/api`,
//   withCredentials: false,
//   headers: {
//     Accept: 'application/json',
//     'Content-type': 'application/json',
//   },
// })
//
// export default {
//   getBlogs() {
//     return apiClient.get('/blogs/')
//   },
//   getBlog(slug) {
//     return apiClient.get(`/blogs/${slug}/`)
//   },
//   postBlog(data) {
//     return apiClient.post('/blogs/', data)
//   },
// }
