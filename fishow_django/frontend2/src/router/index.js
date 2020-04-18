import Vue from 'vue'
import VueRouter from 'vue-router'
const Home = () => import('../views/Home.vue')
const Article = () => import('../views/Article')
const UserPage = () => import('../views/UserPage')
const Blog = () => import('../views/Blog')
const BlogEditor = () => import('../views/BlogEditor')
const CreateComment = () => import('../components/CreateComment')
const NotFound = () => import('../views/NotFound')
const PredictPage = () => import('../views/PredictPage')

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
