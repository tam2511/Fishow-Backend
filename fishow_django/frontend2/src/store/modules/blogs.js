import { apiService } from '../../common/api.service'

export const namespaced = true

export const state = {
  blogs: [],
  next: null,
}

export const mutations = {
  SET_BLOGS(state, blogs) {
    state.blogs = blogs
  },
}

export const actions = {
  fetchBlogs({ commit }) {
    let endpoint = '/api/blogs/'
    if (this.state.next) {
      endpoint = this.state.next
    }
    const blogs = []
    apiService(endpoint).then((data) => {
      blogs.push(...data.results)
      if (data.next) {
        this.state.next = data.next
      } else {
        this.state.next = null
      }
      commit('SET_BLOGS', blogs)
    })
  },
}
