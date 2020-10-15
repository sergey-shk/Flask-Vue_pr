<template>
  <div id="app" class='content'>
    <Header :username='username'/>
    <transition name="fade" mode='out-in'>
      <router-view/>
    </transition>
    <Footer/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'App',
  components: {
    Header,
    Footer
  },
  data () {
    return {
      username: 'User'
    }
  }
}
</script>

<style lang="scss">
@import "@/assets/scss/main";
</style>
