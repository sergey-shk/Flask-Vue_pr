<template>
  <div class="auth_form">
    <input type="text" placeholder='Username' v-model='username'>
    <input type="password" placeholder='Password' v-model='password'>
    <input type="password" placeholder='Confirm your password' v-model='password2'>
    <button v-if='show_button' type="submit" @click.prevent='join'>Join</button>
    <div>
      <div class="">
        <span v-for='msg in msgs' :key='msg'>{{ msg }}<br></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterForm',
  props: [],
  methods: {
    noEr: function () {
      if (this.msgs !== []) {
      } else {
      }
    },
    join () {
      this.$store.dispatch('a/join', {
        username: this.username,
        password: this.password
      })
    }
  },
  data () {
    return {
      username: '',
      password: '',
      password2: '',
      msgs: ['Your username has to be at least 6 characters'],
      msgs_p: ['Your password has to be at least 8 characters'],
      msgsP2: [''],
      show_button: true
    }
  },
  watch: {
    username: function () {
      this.msgs = []
      if (this.username.length < 6) {
        this.msgs.push('Your username has to be at least 6 characters')
        // this.show_button = false
      }
    },
    password: function () {
      this.msgs = []
      if (this.password.length < 8) {
        this.msgs.push('Your password has to be at least 8 characters')
        // this.show_button = false
      }
    },
    password2: function () {
      this.msgs = []
      if (this.password2 !== this.password) {
        this.msgs.push('Passwords mismatch')
      }
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/scss/main.scss';
</style>
