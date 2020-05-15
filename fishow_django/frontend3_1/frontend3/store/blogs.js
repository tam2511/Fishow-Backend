// import { apiService } from '@/plugins/api.service'

import BlogsService from '~/services/BlogsService'

export const state = () => ({
  blogs: [],
  next: null,
})

export const mutations = {
  SET_NEXT(state, next) {
    state.next = next
  },
  SET_BLOGS(state, blogs) {
    state.blogs = blogs
  },
}

export const actions = {
  getBlogs({ commit }) {
    return BlogsService.getBlogs().then((response) => {
      commit('SET_BLOGS', response.data.results)
    })
  },
}
