/*
JavaScript file to initialize the Vue application
Last edited by: Blake Good
Date: 10/30/24
*/
import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

const app = createApp(App)
app.use(router)
app.mount('#app')
