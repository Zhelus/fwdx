<!-- 
Wrapper component for generating/editing reports
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {ref} from 'vue'
    import { useRouter } from 'vue-router'
    import FormSelectionItem from './FormSelectionItem.vue';
    import FormCheckboxItem from './FormCheckboxItem.vue';
    import FormTextInputItem from './FormTextInputItem.vue';
    import FormActionButton from './FormActionButton.vue';
    import FormFrequencyInputItem from './FormFrequencyInputItem.vue';
    
    const props = defineProps(['formTitle', 'showFrequency', 'isEditReport'])
    const router = useRouter();
    const pathogenSelection = ref('Test');
    const reagentSelection = ref('Test');
    const confirmationText = ref('');

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

    function cancelClicked(){
        console.log("Clicked cancel button");
        router.push("/");
    }

    function submitClicked(){
        console.log("Clicked submit button");
    }


</script>
<template>
    <div class="report-form-container">
        <h1 class="form-header">{{ formTitle }}</h1>
        <FormSelectionItem selection-header="Pathogen" :options-list="pathogenOptions" :selection-var="pathogenSelection" select-field="pathogen" @selectionChanged="setSelection"/>
        <FormSelectionItem selection-header="Reagent" :options-list="reagentOptions" :selection-var="reagentSelection" select-field="reagent" @selectionChanged="setSelection"/>
        <FormFrequencyInputItem v-if="showFrequency" section-header="Report Frequency" />
        <FormCheckboxItem section-header="Databases" :options-list="databaseCheckboxOptions" />
        <FormCheckboxItem section-header="Notifications" :options-list="notificationCheckboxOptions" />
        <FormTextInputItem v-model="confirmationText" section-header="Type 'YES' to confirm the above information is correct" />
        <div class="form-button-container">
            <FormActionButton button-text="Cancel" button-class="cancel" @cancelButtonClicked="cancelClicked"/>
            <FormActionButton v-if="isEditReport" v-model="confirmationText" button-text="Save Changes" button-class="submit" @submitButtonClicked="submitClicked"/>
            <FormActionButton v-else v-model="confirmationText" button-text="Submit" button-class="submit" @submitButtonClicked="submitClicked"/>
        </div>
    </div>
</template>
<style scoped>
    .report-form-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        height: auto;
        width: 90%;
        background-color: var(--light-gray-container-background);
        border-radius: 5px;
        padding: 25px;
        overflow-x: scroll;
        /* box-shadow: var(--container-box-shadow); */
        outline: 0.5pt solid var(--light-gray-outline);
    }

    .form-header {
        color: var(--fwdx-blue);
        font-weight: var(--page-header-weight);
        vertical-align: top;
        letter-spacing: -2%;
        font-size: var(--page-header-size);
        line-height: var(--page-header-line-height);
        margin-bottom: var(--form-header-margin);
    }

    .form-button-container {
        display: flex;
        column-gap: var(--form-button-col-gap);
    }
</style>