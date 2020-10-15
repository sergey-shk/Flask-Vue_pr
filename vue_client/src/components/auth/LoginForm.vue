<template>
  <div class="auth_form">
    <input type="text" placeholder='Username' v-model='username'>
    <input type="password" placeholder='Password' v-model='password'>
    <button v-if='show_button' type="submit" @click.prevent='login'>Login</button>
    <div>
      <span v-for='msg in msgs' :key='msg'>{{ msg }}</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  props: [],
  methods: {
    noEr: function () {
      if (this.msgs !== []) {
      } else {
      }
    },
    login () {
      this.$store.dispatch('a/login', {
        username: this.username,
        password: this.password
      })
    }
  },
  data () {
    return {
      username: '',
      password: '',
      msgs: [],
      show_button: true
    }
  },
  watch: {
    username: function () {
      this.msgs = []
      if (this.username.length < 6) {
        this.msgs.push('Username < 6')
        this.show_button = true
      } else {
        this.show_button = true
      }
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/scss/main.scss';
</style>
