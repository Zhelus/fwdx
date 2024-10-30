import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GenerateView from '@/views/GenerateView.vue'
import ScheduleReportView from '@/views/ScheduleReportView.vue'
import EditScheduleView from '@/views/EditScheduleView.vue'
import BrowseReportsView from '@/views/BrowseReportsView.vue'
import PathogensView from '@/views/PathogensView.vue'
import ReagentsView from '@/views/ReagentsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/reports/generate',
      name: 'generate',
      component: GenerateView
    },
    {
      path: '/reports/schedule',
      name: 'schedule',
      component: ScheduleReportView
    },
    {
      path: '/reports/schedule/edit',
      name: 'edit',
      component: EditScheduleView
    },
    {
      path: '/reports/browse',
      name: 'browse',
      component: BrowseReportsView
    },
    {
      path: '/pathogens',
      name: 'pathogens',
      component: PathogensView
    },
    {
      path: '/reagents',
      name: 'reagents',
      component: ReagentsView
    }
  ]
})

export default router
