<script setup>
import { RouterView } from 'vue-router'
import NavigationBar from './components/navigation_bar/NavigationBar.vue'
</script>

<template>
  <!-- Navigation bar component -->
  <NavigationBar/>
  <!-- The rest of the page displayed here 
      -- pages are contained in the '/src/views' folder -->
  <RouterView />
</template>

<style scoped>
</style>
