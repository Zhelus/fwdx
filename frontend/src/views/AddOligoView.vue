<!-- 
Page view for adding a new oligo
Last edited by: Michael Nguyen
Date: 10/30/24
-->
<script setup>
    import AddOligoForm from '@/components/oligos_form/AddOligoForm.vue';
    const formTitle = `Add a new Oligo`;
</script>
<template>
<div class="report-page-wrapper">
    <AddOligoForm form-title="Add a New Oligo" :show-frequency="false" :is-edit-report="true"/>
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