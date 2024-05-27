import { createRouter, createWebHistory } from 'vue-router'
import enthapy from '../components/ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/enthapy',
      name: 'enthapy',
      component: enthapy
    },
  ]
})

export default router