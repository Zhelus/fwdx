<script setup>
import ReportForm from '@/components/ReportForm.vue';
</script>
<template>
<div class="generate-report-wrapper">
    <ReportForm form-title="Generate New Report" />
</div>
</template>
<style scoped>
.generate-report-wrapper {
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