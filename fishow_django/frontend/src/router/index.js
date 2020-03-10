import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Blog from "../views/Blog.vue";
import BlogEditor from "../views/BlogEditor.vue";

Vue.use(Router);

export default new Router ({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/blog/:slug',
      name: 'blog',
      component: Blog,
      props: true
    },
    {
      path: '/blog-editor',
      name: 'blog-editor',
      component: BlogEditor
    }
  ]
});

// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })
//
// export default router
