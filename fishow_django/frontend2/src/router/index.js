import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Article from '../views/Article'
import UserPage from '../views/UserPage'
import Blog from '../views/Blog'
import BlogEditor from '../views/BlogEditor'
import CreateComment from '../components/CreateComment'
import NotFound from '../views/NotFound'
import PredictPage from '../views/PredictPage'
import column from '../components/predictPage/column'
import LoginPage from '../views/LoginPage'
import registration from '../components/registration'
import confirmEmail from '@/views/confirmEmail'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/article/',
    name: 'Article',
    component: Article,
    props: true,
  },
  {
    path: '/predict-page/',
    name: 'PredictPage',
    component: PredictPage,
    props: true,
  },
  {
    path: '/confirm-email/:fishowKey',
    name: 'confirmEmail',
    component: confirmEmail,
    props: true,
  },
  {
    path: '/login/',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/registration/',
    name: 'registration',
    component: registration,
  },
  {
    path: '/predict-page/:areal/:date/:city/:fish',
    name: 'PredictResult',
    component: column,
    props: true,
  },
  {
    path: '/user-page/',
    name: 'UserPage',
    component: UserPage,
    props: true,
  },
  {
    path: '/blog/:slug',
    name: 'blog',
    component: Blog,
    props: true,
  },
  {
    path: '/blog-editor/:slug?',
    name: 'blog-editor',
    component: BlogEditor,
    props: true,
  },
  {
    path: '/comment/:id',
    name: 'Create-comment',
    component: CreateComment,
    props: true,
  },
  {
    path: '*',
    name: 'page-not-found',
    component: NotFound,
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  // base: process.env.BASE_URL,
  routes,
})

export default router
