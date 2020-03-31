<template>
    <article
            class="post-corporate"
    >
        <div class="post-corporate-content">
            <div class="fishow-votes_container">
                <div class="fishow_votes" data-vote-status="">
                    <svg
                            class=""
                            :class="{
              'fishow-votes_up__active': userLikedBlog,
              'fishow-votes_up': !userLikedBlog
            }"
                            @click="toggleLike"
                            version="1.1"
                            id="Capa_1"
                            xmlns="http://www.w3.org/2000/svg"
                            x="0px"
                            y="0px"
                            width="284.929px"
                            height="284.929px"
                            viewBox="0 0 284.929 284.929"
                            xml:space="preserve"
                    >
                        <path
                                d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"
                        />
                      </svg>
                    <svg
                            class=""
                            :class="{
              'fishow-votes_down__active': userDisLikedBlog,
              'fishow-votes_down': !userDisLikedBlog
            }"
                            @click="toggleDislike"
                            version="1.1"
                            id="Capa_1"
                            xmlns="http://www.w3.org/2000/svg"
                            x="0px"
                            y="0px"
                            width="284.929px"
                            height="284.929px"
                            viewBox="0 0 284.929 284.929"
                            xml:space="preserve"
                    >
                        <path
                                d="M282.082,195.285L149.028,62.24c-1.901-1.903-4.088-2.856-6.562-2.856s-4.665,0.953-6.567,2.856L2.856,195.285
		C0.95,197.191,0,199.378,0,201.853c0,2.474,0.953,4.664,2.856,6.566l14.272,14.271c1.903,1.903,4.093,2.854,6.567,2.854
		c2.474,0,4.664-0.951,6.567-2.854l112.204-112.202l112.208,112.209c1.902,1.903,4.093,2.848,6.563,2.848
		c2.478,0,4.668-0.951,6.57-2.848l14.274-14.277c1.902-1.902,2.847-4.093,2.847-6.566
		C284.929,199.378,283.984,197.188,282.082,195.285z"
                        />
                      </svg>
                </div>
                <span data-votes-counter>{{ likesCounter - dislikesCounter }}</span>
                <div class="post-corporate-header">
                    <!-- Badge-->
                    <div class="badge badge-primary">{{ blog.category }}</div>
                    <time class="post-corporate-time"> {{ blog.created_at }} </time>
                    <div class="post-corporate-author">
                        Автор:
                        <span>{{ blog.author }}</span>
                    </div>
                    <div class="post-corporate-view">
                        <span class="icon fl-justicons-visible6"></span>
                        0
                    </div>
                </div>
            </div>

            <h4 class="post-corporate-title">
                <router-link
                        :to="{ name: 'blog', params: { slug: blog.slug } }"
                >{{ blog.title }}</router-link
                >
            </h4>
            <div class="post-corporate-text">
                <div v-for="p in getResult"
                     :key="p.type">
                    <p v-if="p.type === 'text'">{{ p.body }}</p>
                    <iframe v-if="p.type === 'video'" width="560" height="315" :src="p.url" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                    <img v-if="p.type === 'image'" :src="p.url" alt="">
                </div>
            </div>
        </div>
        <a class="post-corporate-figure" href="">
            <img src="" alt="" width="769" height="416" />
        </a>
        <div class="post-corporate-footer">
            <div class="post-corporate-comment">
                <span class="icon mdi mdi-comment-outline"></span>
                <router-link
                        :to="{ name: 'blog', params: { slug: blog.slug } }"
                >{{ blog.comments_count }} Комментариев</router-link
                >
            </div>
            <div class="post-corporate-share">
                <ul class="group">
                    <li>Поделиться</li>
                    <li><a class="icon fa-facebook" href="#"></a></li>
                    <li><a class="icon fa-twitter" href="#"></a></li>
                    <li><a class="icon fa-google-plus" href="#"></a></li>
                    <li><a class="icon fa-instagram" href="#"></a></li>
                </ul>
            </div>
        </div>
    </article>
</template>

<script>
import { apiService } from '../../common/api.service'

export default {
  name: 'BlogCard',
  props: ['blog'],
  data () {
    return {
      result: {},
      userLikedBlog: this.blog.user_has_votedUp,
      userDisLikedBlog: this.blog.user_has_votedDown,
      likesCounter: this.blog.likes_count,
      dislikesCounter: this.blog.dislikes_count
    }
  },
  computed: {
    getResult: function () {
      return JSON.parse(this.blog.content).blocks[0]
    }
  },
  methods: {
    toggleLike () {
      if (this.userLikedBlog) {
        this.unLikeBlog()
      } else {
        if (this.userDisLikedBlog) {
          this.undislikeBlog()
        } else {
          this.likeBlog()
        }
      }
    },
    toggleDislike () {
      if (this.userDisLikedBlog) {
        this.undislikeBlog()
      } else {
        if (this.userLikedBlog) {
          this.unLikeBlog()
        } else {
          this.dislikeBlog()
        }
      }
    },
    likeBlog () {
      this.likesCounter += 1
      this.userLikedBlog = true
      const endpoint = `/api/blogs/${this.blog.id}/like/`
      apiService(endpoint, 'POST')
    },
    unLikeBlog () {
      this.likesCounter -= 1
      this.userLikedBlog = false
      const endpoint = `/api/blogs/${this.blog.id}/like/`
      apiService(endpoint, 'DELETE')
    },
    dislikeBlog () {
      this.dislikesCounter += 1
      this.userDisLikedBlog = true
      const endpoint = `/api/blogs/${this.blog.id}/dislike/`
      apiService(endpoint, 'POST')
    },
    undislikeBlog () {
      this.dislikesCounter -= 1
      this.userDisLikedBlog = false
      const endpoint = `/api/blogs/${this.blog.id}/dislike/`
      apiService(endpoint, 'DELETE')
    }
  }

}
</script>

<style scoped lang="scss">
    .fishow-votes_up__active {
        fill: cadetblue;
    }
    .fishow-votes_down__active {
        fill: red;
    }
    .post-corporate-content  {
        p {
            white-space: pre-line;
        }

    }

</style>
