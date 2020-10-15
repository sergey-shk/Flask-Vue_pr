<template>
  <div class="footer">
    <div class="logo">
      <h1>Appname</h1>
    </div>
    <div class="nav">
      nav
    </div>
    <div class="auth_box">
      <div>
        <router-link @click.native='up' to="/auth">Auth</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  props: ['username'],
  methods: {
    up () {
      window.scrollTo(0, 0)
    }
  }
}
</script>

<style lang="scss">
@import '@/assets/scss/main.scss';
</style>
