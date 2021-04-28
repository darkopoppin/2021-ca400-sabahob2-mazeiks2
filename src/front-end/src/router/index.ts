import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import SignUp from '../views/SignUp.vue';
import SignIn from '../views/SignIn.vue';
import Home from '../views/Home.vue';
import ForgotPassword from '../views/ForgotPassword.vue';
import CategorySelection from '../views/CategorySelection.vue';
import Modal from '../views/Modal.vue';
import Planner from '../views/Planner.vue';
import Settings from '../views/Settings.vue';
import Recommender from '../views/Recommender.vue';
import { auth } from '../firebase';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/SignUp',
    name: 'signUp',
    component: SignUp
  },
  {
    path: '/SignIn',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/ForgotPassword',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  {
    path: '/',
    name: 'Home',
    component: Home,
    children: [
      {
        path: '',
        redirect: 'Categories'
      },
      {
        path: 'Categories',
        component: CategorySelection
      },
      {
        path: 'Planner',
        component: Planner
      },
      {
        path: 'Settings',
        component: Settings
      },
      {
        path: 'Recommender',
        component: Recommender
      },
    ],
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Modal',
    name: 'Modal',
    component: Modal,
    meta: {
      requiresAuth: true
    }
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(x => x.meta.requiresAuth)
  if (requiresAuth && !auth.currentUser) {
    next('/SignIn')
  }
  else {
    next()
  }
})
export default router
