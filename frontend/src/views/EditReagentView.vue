<!-- 
Page view for edit an oligo reagent
Last edited by: Michael Nguyen
Date: 11/05/24
-->
<script setup>
    import EditReagentForm from '@/components/reagents_form/EditReagentForm.vue';
    import { useRoute } from 'vue-router';
    const route = useRoute();
    const productName = route.query.productName || "Product Name";

    const formTitle = `Edit an Oligo - ${productName}`;
</script>
<template>
<div class="report-page-wrapper">
    <EditReagentForm :form-title=formTitle :show-frequency="false" :is-edit-report="false"/>
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