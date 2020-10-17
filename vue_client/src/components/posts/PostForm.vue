<template>
  <div class="post_item mt">
    <div class="user_pic">
    </div>
    <div class="post_body hfix">
      <div class="row1">
        <a class='author'>{{ userdata.username }}</a>
      </div>
      <div class="post_text">
        <textarea class='post_input' v-model="body" placeholder='New post...'></textarea>
      </div>
      <a class='row1 low' @click.prevent='createPost'><span>Post</span></a>
    </div>
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
  },
  computed: {
    userdata () {
      return this.$store.getters['a/getUserData']
    }
  }
}
</script>

<style lang="scss">
</style>
