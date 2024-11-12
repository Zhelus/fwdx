<!-- 
Page view for adding a new product
Last edited by: Michael Nguyen
Date: 11/12/24
-->
<script setup>
    import AddProductForm from '@/components/reagents_form/AddProductForm.vue';
</script>
<template>
<div class="report-page-wrapper">
    <AddProductForm />
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