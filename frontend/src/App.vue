<!-- 
The main application displaying the navigation bar and the current page
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
import { RouterView } from 'vue-router'
import NavigationBar from './components/navigation_bar/NavigationBar.vue'
</script>

<template>
  <!-- Conditionally render the navigation bar if the route is not '/' (LoginView) -->
  <!-- Navigation bar component-->
  <NavigationBar v-if="$route.path !== '/'" />
  <!-- 
  The rest of the page is displayed here 
      - The '.vue' files for each page are contained in the '/src/views' folder 
      - Components used for each page are contained in the '/src/components folder
  -->
  <RouterView />
</template>

<style scoped>
</style>
