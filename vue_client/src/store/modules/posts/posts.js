import axios from 'axios'
export default {
  namespaced: true,

  state: {
    posts: null
  },
  mutations: {
    setposts (state, posts) {
      state.posts = posts
    }
  },
  actions: {
    createPost: ({ commit, dispatch }, postdata) => {
      axios.post('http://127.0.0.1:5000/api/posts/createpost', {
        body: postdata.body
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      }).then(response => (
        dispatch('getPosts')
      ))
    },
    getPosts: ({ commit }) => {
      axios.get('http://127.0.0.1:5000/api/posts/getposts', {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      }).then(response => (
        commit('setposts', response.data.posts)
      ))
    },
    like: ({ commit, dispatch }, postId) => {
      axios.post('http://127.0.0.1:5000/api/posts/like', {
        post_id: postId
      }, {
        headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
      }).then(response => (
        dispatch('getPosts')
      ))
    }
  },
  getters: {
    posts (state) {
      return state.posts
    }
  }
}
