<script setup>
    import FullPageOverlay from '../misc/FullPageOverlay.vue';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import AddPathogenButton from './AddPathogenButton.vue';

    const props = defineProps(['pathogenSelection', 'pathogenOptions']);
    const pathogenModel = defineModel();
    const emit = defineEmits(['pathogenSelected'])
    const testData = [
        {
            pathogenName: "Covid-19",
            sampleCount: "1001",
            ncbiTaxonomyID: "12345"
        },
        {
            pathogenName: "Influenza",
            sampleCount: "1500",
            ncbiTaxonomyID: "56789"
        },
        {
            pathogenName: "RSV",
            sampleCount: "988",
            ncbiTaxonomyID: "98765"
        },
        {
            pathogenName: "JC Polyomavirus",
            sampleCount: 1,
            ncbiTaxonomyID: 10632
        }

    ]

    function assignPathogen(ncbiTaxonomyID, selectedPathogenName){
        console.log(ncbiTaxonomyID);
        console.log(selectedPathogenName)
        pathogenModel.value = {
            pathogenID: ncbiTaxonomyID,
            name: selectedPathogenName
        }
        emit('pathogenSelected')
    }
</script>
<template>
    <FullPageOverlay> 
        <template #TestSlot>
            <div class="pathogen-select-container">
                <div class="pathogen-select-wrapper">
                    <div class="header-wrapper">
                        <h1 class="pathogen-select-header">Select Pathogen</h1>
                        <div class="back-button" @click="$emit('hideOverlayClicked')">&#10005;</div>
                    </div>
                    
                    <DataTable 
                        :value="pathogenOptions"  
                        :rows="10" :rowsPerPageOptions="[5, 10, 15, 20]"
                        paginator
                        paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
                        currentPageReportTemplate="{currentPage} / {totalPages}"
                        removableSort
                        class="overlay-table"
                    >
                        <Column field="common_name" header="Common Name" sortable></Column>
                        <Column field="sampleCount" header="Samples" sortable></Column>
                        <Column field="taxonomicID" header="NCBI Taxonomy ID" sortable></Column>
                        <Column field="taxonomicID" header="Actions">
                            <template #body="slotProps">
                                <AddPathogenButton button-class="table-button" :ncbiTaxonomyID="slotProps.data.taxonomicID" :pathogenName="slotProps.data.common_name" @addPathogenClicked="assignPathogen"/>
                            </template>
                        </Column>
                    </DataTable>
                    <!-- <button @click="$emit('hideOverlayClicked')" class="hide-overlay-button">Go Back</button> -->
                </div>
            </div>
        </template>
    </FullPageOverlay>
</template>
<style scoped>
    .header-wrapper {
        width: 100%;
        height: fit-content;
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1.45em;
        padding-left: .1rem;
    }

    .back-button {
        width: 1.5em;
        height: 1.5em;
        background-color: var(--light-gray-button-bg);
        color: var(--fwdx-blue);
        border-radius: 5px;
        font-weight: 500;
        font-size: 14pt;
        display: flex;
        align-items: center;
        justify-content: center;
        outline: none
    }

    .back-button:hover{
        cursor: pointer;
        background-color: var(--light-gray-button-hover);
        outline: 1pt solid var(--light-gray-button-hover);
        font-weight: 700;
        transition: background-color 0.01s, font-weight 0.01s, outline 0.01s;
    }

    .pathogen-select-container {
        width: 100%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .pathogen-select-wrapper {
        width: 100%;
        height: 100%;
        /* max-height: 90%; */
        display: flex;
        flex-direction: column;
        justify-content: left;
        align-items: flex-start;
        background-color: white;
        box-shadow: 0px 4px 20px -10px var(--fwdx-blue);
        border-radius: 5px;
        line-height: var(--page-header-line-height);
        margin-bottom: var(--form-header-margin);
        padding: var(--form-padding);
    }

    .pathogen-select-header {
        font-size: var(--page-header-size);
        font-weight: var(--page-header-weight);
        color: var(--fwdx-blue);
        /* margin-bottom: var(--form-header-margin); */
    }

    .hide-overlay-button {
        border: none;
        background-color: #eaeaea;
        color: var(--fwdx-blue);
        width: auto;
        padding: 0.5rem;
        font-size: var(--body-text-size);
        font-weight: 600;
        border-radius: 5px;
    }

    .hide-overlay-button:hover {
        cursor: pointer;
        background-color: #e0e0e0;
        transition: 0.1s;
    }
</style>