<!-- 
Page view for adding a new oligo
Last edited by: Michael Nguyen
Date: 10/30/24
-->
<script setup>
    import AddOligoForm from '@/components/oligos_form/AddOligoForm.vue';
    import { useRoute } from 'vue-router';
    const route = useRoute();
    const productName = route.query.productName || "Product Name";

    const formTitle = `Add a new Oligo - ${productName}`;
</script>
<template>
<div class="report-page-wrapper">
    <AddOligoForm/>
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