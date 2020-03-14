import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Blog from "../views/Blog.vue";
import BlogEditor from "../views/BlogEditor.vue";
import CreateComment from "../components/CreateComment.vue";
import NotFound from "../views/NotFound.vue";
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
      path: '/blog-editor/:slug?',
      name: 'blog-editor',
      component: BlogEditor,
      props: true
    },
    {
      path:"/comment/:id",
      name: "Create-comment",
      component: CreateComment,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound
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
