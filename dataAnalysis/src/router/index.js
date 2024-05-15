import { createRouter, createWebHistory } from 'vue-router'
import test from '../components/ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/test',
      name: 'test',
      component: test
    },
  ]
})

export default router