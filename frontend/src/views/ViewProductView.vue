<!-- 
Page view for viewing a single oligo
Last edited by: Michael Nguyen
Date: 11/28/24
-->
<script setup>
    import ViewProductForm from '@/components/products_form/ViewProductForm.vue';
</script>
<template>
<div class="report-page-wrapper">
    <ViewProductForm />
</div>
</template>
<style scoped>
.report-page-wrapper {
    min-height: 100%;
    height: 100%;
    max-height: 100%;
    background-color: var(--gray-page-background);
    padding: 2rem;
    min-width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
}
</style>