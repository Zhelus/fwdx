<!-- 
Wrapper component for generating/editing reports
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {ref} from 'vue'
    import { useRouter } from 'vue-router'
    import { onBeforeMount } from 'vue';
    import FormSelectionItem from './FormSelectionItem.vue';
    import FormCheckboxItem from './FormCheckboxItem.vue';
    import FormTextInputItem from './FormTextInputItem.vue';
    import FormActionButton from './FormActionButton.vue';
    import FormFrequencyInputItem from './FormFrequencyInputItem.vue';
    import PathogenSelectOverlay from './PathogenSelectOverlay.vue';
    import ReagentSelectOverlay from './ReagentSelectOverlay.vue';
    import LoadingIcon from '../misc/LoadingIcon.vue';
    import apiClient from '@/services/apiClient';
    import reportsApiHelper from '@/services/reportsApiHelper';
    
    const props = defineProps(['formTitle', 'showFrequency', 'isEditReport'])
    const router = useRouter();
    const pathogenSelection = ref('Test');
    const reagentSelection = ref('Test');
    const confirmationText = ref('');
    const reportTitle = ref('');
    const buttonIsDisabled = ref(true);
    const showPathogenOverlay = ref(false);
    const showReagentOverlay = ref(false);
    const pathogens = ref() 
    const initComplete = ref(false)

    onBeforeMount(() => {
        console.log("BEFORE MOUNT")
        reportsApiHelper.getUniquePathogens()
            .then(data => {
                pathogens.value = data
                initComplete.value = true
            })
            .catch(error => {
                console.error(error);
            })
    })

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
        updateDisabled();
        
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

    function updateDisabled() {
        if(reportTitle.value !== '' && pathogenSelection.value !== 'Test' && reagentSelection.value !== 'Test' && confirmationText.value === 'YES'){
            buttonIsDisabled.value = false;
        }
        else{
            buttonIsDisabled.value = true;
        }
    }

    function showPathogenSelect(){
        showPathogenOverlay.value = !showPathogenOverlay.value;
    }

    function showReagentSelect(){
        showReagentOverlay.value = !showReagentOverlay.value;
    }

    function assignPathogen(ncbiTaxonomyID){
        console.log(ncbiTaxonomyID);
    }

    function cancelClicked(){
        console.log("Clicked cancel button");
        router.push("/");
    }
    
    function getSMN() {
        console.log(pathogenSelection.value);
        console.log(reagentSelection.value);
        let requestData = {
            NCBI_taxonomy_ID: pathogenSelection.value.pathogenID,
            product: {
                oligos: ["AATGCAACAGTGCAATCTCA", "GGCCCAACACCAAATTCATC", "TTGGGTTCCTGATCCCACCAG", "AAGTACATGCCCATAAGCAA", "AGACAGCCATATGCAGTAG", "AAACCTGCTTAGTTTCTTCTGGTTCTT"],
                metadata: "Extra data"
            }
        }
        console.log(requestData);

        apiClient.generateReport({data: requestData})
            .then(data => {
                console.log(data);
            })
            .catch(error => {
                console.error(error);
            })
    }


</script>
<template>
    <LoadingIcon :init-complete="initComplete" />
    <Transition name="form">
        <div v-if="initComplete" class="report-form-container">
            <h1 class="form-header">{{ formTitle }}</h1>
            <FormTextInputItem v-model="reportTitle" section-header="Title" input-type="title" @inputTextChanged="updateDisabled()"/>
            <FormSelectionItem select-type="table" selection-header="Pathogen" :options-list="pathogenOptions" :selection-var="pathogenSelection" select-field="pathogen" @selectionChanged="setSelection" @selectButtonClicked="showPathogenSelect"/>
            <Transition>
                <PathogenSelectOverlay v-if="showPathogenOverlay" v-model="pathogenSelection" :pathogen-options="pathogens" @pathogenSelected="showPathogenSelect" @hideOverlayClicked="showPathogenSelect" />
            </Transition>
            <FormSelectionItem select-type="table" selection-header="Product" :options-list="reagentOptions" :selection-var="reagentSelection" select-field="reagent" @selectionChanged="setSelection" @selectButtonClicked="showReagentSelect"/>
            <Transition>
                <ReagentSelectOverlay v-if="showReagentOverlay" v-model="reagentSelection" @productSelected="showReagentSelect" @hideOverlayClicked="showReagentSelect" />
            </Transition>
            <FormFrequencyInputItem v-if="showFrequency" section-header="Report Frequency" />
            <!-- <FormCheckboxItem section-header="Databases" :options-list="databaseCheckboxOptions" /> -->
            <FormCheckboxItem section-header="Notifications" :options-list="notificationCheckboxOptions" />
            <FormTextInputItem v-model="confirmationText" input-type="confirmation" is-confirmation="true" section-header="Type 'YES' to confirm the above information is correct" @confirmationTextChanged="updateDisabled()"/>
            <div class="form-button-container">
                <FormActionButton button-text="Cancel" button-class="cancel" @cancelButtonClicked="cancelClicked"/>
                <FormActionButton v-if="isEditReport" v-model="confirmationText" button-text="Save Changes" button-class="submit" @submitButtonClicked="submitClicked"/>
                <FormActionButton v-else v-model:confirmationText="confirmationText" v-model:buttonIsDisabled="buttonIsDisabled" button-text="Submit" button-class="submit" @submitButtonClicked="getSMN()"/>
            </div>
        </div>
    </Transition>
</template>
<style scoped>
    .form-enter-active{
        transition: opacity 0.25s ease;
    }

    .form-leave-active {
        transition: opacity 0.25s ease;
    }

    .form-enter-from, .v-leave-to {
        opacity: 0;
    }

    .v-enter-active{
        transition: opacity 0.15s ease;
    }

    .v-leave-active {
        transition: opacity 0.05s ease;
    }

    .v-enter-from, .v-leave-to {
        opacity: 0;
    }

    .report-form-container {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        height: auto;
        width: 90%;
        background-color: var(--light-gray-container-background);
        border-radius: 5px;
        padding: var(--form-padding);
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