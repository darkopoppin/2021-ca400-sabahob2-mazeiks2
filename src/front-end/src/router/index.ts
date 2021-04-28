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
        redirect: 'categories'
      },
      {
        path: 'categories',
        component: () => import('@/views/CategorySelection.vue')
      },
      {
        path: 'mobilePlanner',
        component: () => import('@/views/Planner.vue')
      },
      {
        path: 'mobileSettings',
        component: () => import('@/views/Settings.vue')
      },
    ],
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/CategorySelection',
    name: 'CategorySelection',
    component: CategorySelection,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Settings',
    name: 'Settings',
    component: Settings,
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
  {
    path: '/planner',
    name: 'Planner',
    component: Planner,
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
