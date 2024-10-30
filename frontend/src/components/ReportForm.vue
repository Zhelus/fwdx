<!-- 
Wrapper component for generating/editing reports
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {ref} from 'vue'
    import FormSelectionItem from './FormSelectionItem.vue';
    import FormCheckboxItem from './FormCheckboxItem.vue';
    
    const props = defineProps(['formTitle'])
    const pathogenSelection = ref('Test');
    const reagentSelection = ref('Test');

    const pathogenOptions = [
        {
            value: 'rsv',
            name: 'RSV'
        },
        {
            value: 'influenza',
            name: 'Influenza'
        },
        {
            value: 'SARS-CoV-2',
            name: 'Covid'
        }
    ];

    const reagentOptions = [
        {
            value: 'rsv',
            name: 'RSV'
        },
        {
            value: 'influenza',
            name: 'Influenza'
        },
        {
            value: 'SARS-CoV-2',
            name: 'Covid'
        }
    ];

    function setSelection(newSelection, selectField) {  
        if(selectField == 'pathogen'){
            pathogenSelection.value = newSelection;
            console.log(pathogenSelection.value);
        }
        if(selectField == 'reagent'){
            reagentSelection.value = newSelection;
            console.log(reagentSelection.value);
        }
        
    }

    const databaseCheckboxOptions = [
        {
            name: "NCBI",
            value: 'ncbi'
        },
        {
            name: "GISAID",
            value: 'gisaid'
        },
        {
            name: "SIB ViralZone",
            value: 'sib_viralzone'
        },
        {
            name: "BV-BRC",
            value: 'bv-brc'
        },
        {
            name: "SILVA rRNA",
            value: 'silva_rrna'
        },
        {
            name: "VuePathDB",
            value: 'vuepathdb'
        }
    ];

    const notificationCheckboxOptions = [
        {
            name: "Email",
            value: 'email'
        },
        {
            name: "Text",
            value: 'text'
        }
    ];


</script>
<template>
    <div class="report-form-container">
        <h1 class="form-header">{{ formTitle }}</h1>
        <!-- <p style="color: black;">{{ pathogenSelection }}</p>
        <p style="color: black;">{{ reagentSelection }}</p> -->
        <FormSelectionItem selection-header="Pathogen" :options-list="pathogenOptions" :selection-var="pathogenSelection" select-field="pathogen" @selectionChanged="setSelection"/>
        <FormSelectionItem selection-header="Reagent" :options-list="reagentOptions" :selection-var="reagentSelection" select-field="reagent" @selectionChanged="setSelection"/>
        <FormCheckboxItem section-header="Databases" :options-list="databaseCheckboxOptions" />
        <FormCheckboxItem section-header="Notifications" :options-list="notificationCheckboxOptions" />

    </div>
</template>
<style scoped>
    .report-form-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        height: 90%;
        width: 90%;
        background-color: var(--light-gray-container-background);
        border-radius: 5px;
        padding: 25px;
    }

    .form-header {
        color: var(--fwdx-blue);
        font-weight: 700;
        vertical-align:top;
        letter-spacing: -2%;
        font-size: 26pt;
        line-height: 0.95em;
        margin-bottom: 2.5rem;
    }
</style>