<template>
  <div class="header">
    <div class="logo">
    </div>
    <div class="nav">
      <router-link to="/">Feed</router-link>
      <router-link to="/about">About</router-link>
      <div v-if='isAuth === true'>
        <a>{{ userdata.username }}</a>
      </div>
      <div v-if='isAuth === true'>
        <a @click.prevent='logout'>Logout</a>
      </div>
      <div v-else class='auth_b'>
        <router-link to="/auth">Auth</router-link>
      </div>
    </div>
    <div class="auth_box">
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header',
  props: [],
  data () {
    return {
    }
  },
  methods: {
    logout () {
      this.$store.dispatch('a/logout')
    }
  },
  computed: {
    isAuth () {
      return this.$store.getters['a/isAuth']
    },
    userdata () {
      return this.$store.getters['a/getUserData']
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss">
// @import '@/assets/scss/main.scss';
</style>
