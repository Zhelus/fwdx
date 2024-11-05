<!-- 
Page view for adding a new reagent
Last edited by: Michael Nguyen
Date: 10/30/24
-->
<script setup>
    import AddReagentForm from '@/components/reagents_form/ReagentForm.vue';
    import { useRoute } from 'vue-router';
    const route = useRoute();
    const productName = route.query.productName || "Product Name";

    const formTitle = `Add a new Oligo - ${productName}`;
</script>
<template>
<div class="report-page-wrapper">
    <AddReagentForm :form-title=formTitle :show-frequency="false" :is-edit-report="false"/>
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