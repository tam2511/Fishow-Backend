<template>
  <div class="home">

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { apiService } from "../common/api.service";

export default {
  name: 'Home',
  data() {
      return {
          blogs: []
      }
  },
  methods: {
      getBlogs() {
          let endpoint = "api/blogs/";
          apiService(endpoint)
            .then(data => {
                this.blogs.push(...data.results);
            })
      }
  }
}
</script>
