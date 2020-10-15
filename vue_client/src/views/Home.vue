<template>
  <div class="page">
    <div v-if='isAuth'>
      <span>Join as {{ userdata.username }}</span><br>
      <span>Id {{ userdata.id }}</span>
    </div>
    <span>{{ msg }}</span>
    <div class="posts_list">
      <PostForm/>
      <br>
      <div class="post_item" v-for='post in posts' :key='post.id'>
        <span>{{ post.authors_username }}</span>
        <h2>{{ post.body }}</h2>
        <span style='font-size: 16px;'>{{ post.liked_users.length }}</span>
        <a v-if='post.author_id !== userdata.id' @click.prevent='like(post.id)'>Like</a>
        <hr>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PostForm from '@/components/posts/PostForm.vue'
export default {
  name: 'Home',
  data () {
    return {
      msg: ''
    }
  },
  methods: {
    like (postId) {
      this.$store.dispatch('p/like', postId)
    }
  },
  components: {
    PostForm
  },
  computed: {
    userdata () {
      return this.$store.getters['a/getUserData']
    },
    isAuth () {
      return this.$store.getters['a/isAuth']
    },
    posts () {
      return this.$store.getters['p/posts']
    }
  },
  created () {
    this.$store.dispatch('a/autologin')
    this.$store.dispatch('p/getPosts')
  }
}
</script>
