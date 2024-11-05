/*
JavaScript file to initialize the Vue application
Last edited by: Blake Good
Date: 11/5/24
*/
import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config'
import router from './router'

const app = createApp(App)
app.use(router)
// Add PrimeVue to the application
// -- The 'pt' (passthrough) option allows us to manipulate the DOM of PrimeVue components
app.use(PrimeVue, {
    pt: {
        datatable: {
            tablecontainer: {
                class: 'table-container'
            },
            table: {
                class: 'table-element'
            },
            thead: {
                class: 'table-head'
            },
            tbody: {
                class: 'table-body'
            },
            headerrow: {
                class: 'table-head-row'
            },
            headercell: {
                class: 'table-head-cell'
            },
            bodyrow: {
                class: 'body-row'
            }
        },
        column: {
            bodycell: {
                class: 'body-cell'
            },
            headercell: {
                class: 'header-cell'
            }
        }
    },
    theme: 'none'
});
app.mount('#app')
