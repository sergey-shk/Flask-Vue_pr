import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth/auth'
import posts from './modules/posts/posts'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    a: auth,
    p: posts
  }
})
