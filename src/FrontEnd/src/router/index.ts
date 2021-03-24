import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import SignUp from '../views/SignUp.vue';
import SignIn from '../views/SignIn.vue';
import Home from '../views/Home.vue';
import ForgotPassword from '../views/ForgotPassword.vue';
import CategorySelection from '../views/CategorySelection.vue';
import Modal from '../views/Modal.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/SignUp',
    name: 'signUp',
    component: SignUp
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/ForgotPassword',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/CategorySelection',
    name: 'CategorySelection',
    component: CategorySelection
  },
  {
    path: '/Modal',
    name: 'Modal',
    component: Modal
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
