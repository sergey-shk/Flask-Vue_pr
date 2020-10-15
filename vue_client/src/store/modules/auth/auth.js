import axios from 'axios'
import router from '@/router'
export default {
  namespaced: true,

  state: {
    username: null,
    token: null,
    id: null,
    date_of_birth: null
  },
  mutations: {
    authUser (state, userData) {
      state.username = userData.username
      state.token = userData.token
      state.id = userData.id
      state.date_of_birth = userData.date_of_birth
    },
    clearAuthData (state) {
      state.username = null
      state.token = null
      state.id = null
      state.date_of_birth = null
    }
  },
  actions: {
    join: ({ commit }, userData) => {
      axios.post('http://127.0.0.1:5000/api/users/signup', {
        username: userData.username,
        password: userData.password
      }).then(response => {
        commit('authUser', response.data[0])
        localStorage.setItem('token', response.data[0].token)
        localStorage.setItem('username', response.data[0].username)
        router.push('/')
      })
    },
    login: ({ commit }, userData) => {
      axios.post('http://127.0.0.1:5000/api/users/login', {
        username: userData.username,
        password: userData.password
      }).then(response => {
        commit('authUser', response.data[0])
        localStorage.setItem('token', response.data[0].token)
        localStorage.setItem('username', response.data[0].username)
        router.push('/')
      })
    },
    logout: ({ commit }) => {
      commit('clearAuthData')
      localStorage.removeItem('username')
      localStorage.removeItem('token')
      router.push('/auth')
    },
    autologin: ({ commit, state }) => {
      if (!localStorage.getItem('token')) {
        return router.replace('/auth')
      }
      commit('authUser', {
        username: localStorage.getItem('username'),
        token: localStorage.getItem('token'),
        id: state.id,
        date_of_birth: state.date_of_birth
      })
    }
  },
  getters: {
    isAuth (state) {
      return state.token !== null
    },
    getUserData (state) {
      return {
        username: state.username,
        id: state.id,
        date_of_birth: state.date_of_birth
      }
    }
  }
}
