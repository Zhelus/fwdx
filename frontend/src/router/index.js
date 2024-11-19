/*
JavaScript file to define the URL paths for each page (used by the Vue router)
Last edited by: Blake Good
Date: 10/30/24
*/
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GenerateView from '@/views/GenerateView.vue'
import ScheduleReportView from '@/views/ScheduleReportView.vue'
import EditScheduleView from '@/views/EditScheduleView.vue'
import BrowseReportsView from '@/views/BrowseReportsView.vue'
import PathogensView from '@/views/PathogensView.vue'
import ReagentsView from '@/views/ReagentsView.vue'
import FlaskExampleView from "@/views/FlaskExampleView.vue";
import AddReagentView from '@/views/AddReagentView.vue'
import EditReagentView from '@/views/EditReagentView.vue'
import AccountView from "@/views/AccountView.vue";
import AddAccountView from "@/views/AddAccountView.vue";
import EditAccountView from "@/views/EditAccountView.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import ForgotPasswordView from "@/views/ForgotPasswordView.vue";

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
      component: AddReagentView
    },
    {
      path:'/reagents/edit',
      name:'editReagent',
      component: EditReagentView
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
