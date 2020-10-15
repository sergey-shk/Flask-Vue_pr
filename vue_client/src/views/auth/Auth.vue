<template>
  <div class='page'>
    <div v-if='ch' class='auth_box'>
      <LoginForm/><br>
      <span>Don't have an account?<br><a @click.prevent='changebox'>Join</a></span>
    </div>
    <div v-else class='auth_box'>
      <RegisterForm/><br>
      <a @click.prevent='changebox'>Login</a>
    </div>
  </div>
</template>

<script>
import RegisterForm from '@/components/auth/RegisterForm.vue'
// @ is an alias to /src
import LoginForm from '@/components/auth/LoginForm.vue'
export default {
  name: 'Auth',
  components: {
    LoginForm,
    RegisterForm
  },
  data () {
    return {
      ch: true
    }
  },
  methods: {
    changebox () {
      this.ch = !this.ch
    }
  }
}
</script>
