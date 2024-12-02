<script setup>
    import { onMounted } from 'vue';
</script>
<template>
    <div class="page-overlay-container">
        <slot name="TestSlot"></slot>
    </div>
</template>
<style scoped>
.page-overlay-container {
    width: 100vw;
    height: 100vh;
    position: absolute;
    padding: 7.5vh;
    top: 0;
    left: 0;
    z-index: 200;
    background-color: rgba(0, 0, 0, 0.5);
}
</style>