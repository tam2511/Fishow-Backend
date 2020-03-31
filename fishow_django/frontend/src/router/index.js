import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Blog from '../views/Blog.vue'
import BlogEditor from '../views/BlogEditor.vue'
import CreateComment from '../components/CreateComment.vue'
import NotFound from '../views/NotFound.vue'
import Article from '../views/Article'
import UserPage from '../views/UserPage'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/article/',
      name: 'Article',
      component: Article,
      props: true
    },
    {
      path: '/user-page/',
      name: 'UserPage',
      component: UserPage,
      props: true
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
      path: '/comment/:id',
      name: 'Create-comment',
      component: CreateComment,
      props: true
    },
    {
      path: '*',
      name: 'page-not-found',
      component: NotFound
    }
  ]
})
