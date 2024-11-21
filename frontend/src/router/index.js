/*
JavaScript file to define the URL paths for each page (used by the Vue router)
Last edited by: Michael Nguyen
Date: 11/21/24
*/
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GenerateView from '@/views/GenerateView.vue'
import ScheduleReportView from '@/views/ScheduleReportView.vue'
import EditScheduleView from '@/views/EditScheduleView.vue'
import BrowseReportsView from '@/views/BrowseReportsView.vue'
import PathogensView from '@/views/PathogensView.vue'
import ReagentsView from '@/views/ProductsHomeView.vue'
import FlaskExampleView from "@/views/FlaskExampleView.vue";
import AddProductView from '@/views/AddProductView.vue'
import OligosHomeView from '@/views/OligosHomeView.vue'
import AccountView from "@/views/AccountView.vue";
import AddAccountView from "@/views/AddAccountView.vue";
import EditAccountView from "@/views/EditAccountView.vue";
import AddOligoView from '@/views/AddOligoView.vue'
import SingleOligoView from '@/views/SingleOligoView.vue'

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
    },
    { 
      path: '/reagents/add', 
      name:'addReagent',
      component: AddProductView
    },
    {
      path: '/reagents/addProduct',
      name: 'addProduct',
      component: AddProductView
    },
    {
      path: '/oligos',
      name: 'oligos',
      component: OligosHomeView
    },
    {
      path: '/oligos/add',
      name: 'addOligo',
      component: AddOligoView
    },
    {
      path: '/oligos/view',
      name: 'viewOligo',
      component: () => import('@/views/SingleOligoView.vue'), // Lazy load the component
      props: route => ({ id: route.query.id }) // Pass the 'id' from the query as a prop
    },        
    {
      path: '/flaskExample',
      name: 'flaskExample',
      component: FlaskExampleView
    },
    {
      path: '/accounts',
      name: 'accounts',
      component: AccountView
    },
    {
      path: '/accounts/add',
      name: 'addAccount',
      component: AddAccountView
    },
    {
      path: '/accounts/edit',
      name: 'editAccount',
      component: EditAccountView
    }
  ]
})

export default router
