<script setup>
    import AddpathogenForm from '@/components/pathogens_form/AddPathogenForm.vue';
    const formTitle = `Add a new pathogen`;
</script>
<template>
<div class="report-page-wrapper">
    <AddpathogenForm form-title="Add a New pathogen" :show-frequency="false" :is-edit-report="true"/>
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