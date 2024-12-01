<!-- 
Page view for viewing a single oligo
Last edited by: Michael Nguyen
Date: 11/28/24
-->
<script setup>
    import ViewOligoForm from '@/components/oligos_form/ViewOligoForm.vue';
</script>
<template>
<div class="report-page-wrapper">
    <ViewOligoForm />
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