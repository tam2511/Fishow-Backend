// import { apiService } from '@/plugins/api.service'

import axios from '~/.nuxt/axios'

export const state = () => ({
  blogs: [],
  next: null
})

export const mutations = {
  SET_NEXT(state, next) {
    state.next = next
  },
  SET_BLOGS(state, blogs) {
    state.blogs = blogs
  }
}

export const actions = {
  async fetchBlogs({ commit }) {
    let endpoint = '/api/blogs/'

    if (this.state.blogs.next) {
      endpoint = this.state.blogs.next
    }
    // let next = null
    // const blogs = []
    const { data } = await axios.get(endpoint)
    console.log('data = ', data)
    commit('SET_BLOGS', data)

    // apiService(endpoint).then(data => {
    //   // this.state.blogs.blogs.push(...data.results)
    //   blogs.push(...data.results)
    //   if (data.next) {
    //     next = data.next
    //   } else {
    //     next = null
    //   }
    //   commit('SET_BLOGS', blogs)
    //   // commit('SET_BLOGS', this.state.blogs.blogs)
    //   commit('SET_NEXT', next)
    // })
  }
}
