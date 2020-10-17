<template>
  <div class="page">
    <span>{{ msg }}</span>
    <div class="posts_list">
      <PostForm/>
      <br>
      <div class="post_item" v-for='post in posts' :key='post.id'>
        <div class="user_pic">
        </div>
        <div class="post_body">
          <div class='row1'>
            <a class='author'>{{ post.authors_username }}</a>
            <span style='font-size: 18px;'>{{ post.pub_time }}</span>
          </div>
          <span class='post_text'>{{ post.body }}</span>
          <div class="row1 low">
            <a @click.prevent='like(post.id)'><div class='plus_btn'>+</div></a>
            <span>{{ post.liked_users.length }}</span>
            <a @click.prevent='like(post.id)'><div class='plus_btn'>-</div></a>
          </div>
        </div>
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
