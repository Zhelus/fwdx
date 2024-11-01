<!-- 
Page view for creating a new scheduled report
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import ReportForm from '@/components/report_form/ReportForm.vue';
</script>
<template>
<div class="report-page-wrapper">
    <ReportForm form-title="Schedule New Report" :show-frequency="true" :is-edit-report="false"/>
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