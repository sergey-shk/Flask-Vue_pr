<template>
  <div class="post_form">
    <textarea class='post_input' v-model="body" placeholder='Tell us something'></textarea>
    <a @click.prevent='createPost'>Publish</a>
  </div>
</template>

<script>
export default {
  name: 'PostForm',
  props: [],
  data () {
    return {
      body: ''
    }
  },
  methods: {
    createPost () {
      this.$store.dispatch('p/createPost', {
        body: this.body
      })
      // if msg is ok -> clear textarea
      this.body = ''
    }
  }
}
</script>

<style lang="scss">
</style>
