/*
JavaScript file to define the URL paths for each page (used by the Vue router)
Last edited by: Nicholas Tullbane
Date: 11/25/24
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
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import ForgotPasswordView from "@/views/ForgotPasswordView.vue";
import AddOligoView from '@/views/AddOligoView.vue'
import SingleOligoView from '@/views/ViewOligoVIew.vue'
import ViewReportView from '@/views/ViewReportView.vue'
import ViewProductView from '@/views/ViewProductView.vue'
import EditProductView from '@/views/EditProductView.vue'
import PathogensDetailedView from '@/views/PathogensDetailedView.vue'
import AddPathogenView from '@/views/AddPathogenView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/forgot_password',
      name: 'forgot_password',
      component: ForgotPasswordView
    },
    {
      path: '/reports',
      name: 'home',
      component: HomeView
    },
    {
      path: '/reports/view/:testProps',
      name: 'viewReport',
      component: ViewReportView,
      props: true
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
      path: '/pathogens/view', // Path for the detailed view
      name: 'PathogenDetailView',
      component: PathogensDetailedView,
    },
    {
      path: '/pathogens/add',
      name: 'addPathogen',
      component: AddPathogenView
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
      path: '/reagents/view/:productId',
      name: 'viewProduct',
      component: ViewProductView,
      props: true,
    },
    {
      path: '/reagents/edit/:productId',
      name: 'editProduct',
      component: EditProductView,
      props: true,
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
      component: () => import('@/views/ViewOligoVIew.vue'), // Lazy load the component
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
      path: '/accounts/edit/:userId',
      name: 'editAccount',
      component: EditAccountView
    }
  ]
})

export default router
