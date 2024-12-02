<script setup>
    import AddPathogenForm from '@/components/pathogens_form/AddPathogenForm.vue';
</script>

<template>
<div class="report-page-wrapper">
    <AddPathogenForm form-title="Add a New Pathogen"/>
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