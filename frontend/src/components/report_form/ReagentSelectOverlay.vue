<script setup>
    import FullPageOverlay from '../misc/FullPageOverlay.vue';
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import AddProductButton from './AddProductButton.vue';

    const props = defineProps(['productSelection']);
    const productSelected = defineModel();
    const emit = defineEmits(['productSelected'])
    const testData = [
        {
            productName: "Product 1",
            oligoCount: "5",
            oligos: ["AATGCAACAGTGCAATCTCA", "GGCCCAACACCAAATTCATC", "TTGGGTTCCTGATCCCACCAG", "AAGTACATGCCCATAAGCAA", "AGACAGCCATATGCAGTAG", "AAACCTGCTTAGTTTCTTCTGGTTCTT"],
            metadata: "Extra Data"
        },{
            productName: "Product 2",
            oligoCount: "5",
            oligos: ["AATGCAACAGTGCAATCTCA", "GGCCCAACACCAAATTCATC", "TTGGGTTCCTGATCCCACCAG", "AAGTACATGCCCATAAGCAA", "AGACAGCCATATGCAGTAG", "AAACCTGCTTAGTTTCTTCTGGTTCTT"],
            metadata: "Extra Data"
        },{
            productName: "Product 3",
            oligoCount: "5",
            oligos: ["AATGCAACAGTGCAATCTCA", "GGCCCAACACCAAATTCATC", "TTGGGTTCCTGATCCCACCAG", "AAGTACATGCCCATAAGCAA", "AGACAGCCATATGCAGTAG", "AAACCTGCTTAGTTTCTTCTGGTTCTT"],
            metadata: "Extra Data"
        },{
            productName: "Product 4",
            oligoCount: "5",
            oligos: ["AATGCAACAGTGCAATCTCA", "GGCCCAACACCAAATTCATC", "TTGGGTTCCTGATCCCACCAG", "AAGTACATGCCCATAAGCAA", "AGACAGCCATATGCAGTAG", "AAACCTGCTTAGTTTCTTCTGGTTCTT"],
            metadata: "Extra Data"
        }
    ]

    function assignProduct(oligos, metadata, productName){
        console.log(oligos);
        console.log(metadata)
        productSelected.value = {
            oligos: oligos,
            metadata: metadata,
            name: productName
        }
        emit('productSelected')
    }
</script>
<template>
    <FullPageOverlay> 
        <template #TestSlot>
            <div class="pathogen-select-container">
                <div class="pathogen-select-wrapper">
                    <div class="header-wrapper">
                        <h1 class="pathogen-select-header">Select Product</h1>
                        <div class="back-button" @click="$emit('hideOverlayClicked')">&#10005;</div>
                    </div>
                    <DataTable 
                        :value="testData"  
                        :rows="10" :rowsPerPageOptions="[5, 10, 15, 20]"
                        paginator
                        paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
                        currentPageReportTemplate="{currentPage} / {totalPages}"
                        removableSort
                        class="overlay-table"
                    >
                        <Column field="productName" header="Product Name" sortable></Column>
                        <Column field="oligoCount" header="Oligo Count" sortable></Column>
                        <Column field="metadata" header="Metadata" sortable></Column>
                        <Column field="oligos" header="Actions">
                            <template #body="slotProps">
                                <AddProductButton button-class="table-button" :oligos="slotProps.data.oligos" :metadata="slotProps.data.metadata" :product-name="slotProps.data.productName" @addProductClicked="assignProduct"/>
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
        width: 90%;
        height: auto;
        max-height: 90%;
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