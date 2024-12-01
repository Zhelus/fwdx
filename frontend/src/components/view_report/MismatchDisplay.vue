<script setup>
    import { ref, onMounted, onBeforeMount, onUpdated } from 'vue'
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';

    const props = defineProps(['mismatch', 'mismatches']);
    const sequenceCharClassName = ref("")
    const activeMismatch = ref({});
    const displayMismatch = ref(false);

    // Set a new active mismatch
    function changeActiveMismatch(groupIndex){
        activeMismatch.value = props.mismatches[groupIndex];
    }

    function toggleMismatchDisplay(){
        displayMismatch.value = !displayMismatch.value;
    }

    function setDisplayWidths(){
        let numChars = activeMismatch.value.oligoSequence.length;
        let widthPercentage = 100/numChars;
        let chars = document.getElementsByClassName(sequenceCharClassName.value);
        for(let i=0; i<chars.length; i++){
            chars[i].style.width = `${widthPercentage}%`;
        }
    }

    // Update display sizing after setting a new active mismatch
    onUpdated(() => {
        setDisplayWidths();

    })

    // Set the first mismatch as "active"
    onBeforeMount(() => {
        activeMismatch.value = props.mismatches[0];
        sequenceCharClassName.value = `${activeMismatch.value.oligoName.replaceAll(' ', '')}-sequence-char`
    })

    // Set the size of each mismatch character
    onMounted(() => {
        setDisplayWidths();
    })
</script>
<template>
    <div class="mismatch-container">
        <div class="mismatch-title-wrapper" @click="toggleMismatchDisplay">
            <img class="inline-icon" src="../icons/dna-icon.svg"></img>
            <h3 class="mismatch-title">{{ activeMismatch.oligoName }}</h3>

        </div>
        <div v-if="displayMismatch" class="mismatch-content-wrapper">
            <DataTable 
                :value="mismatches"  
                :rows="5" :rowsPerPageOptions="[5, 10, 15, 20]"
                paginator
                paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
                currentPageReportTemplate="{currentPage} / {totalPages}"
                removableSort
                class="mismatch-table"
            >
                <Column field="pathogenCommonName" header="Common Name" sortable></Column>
                <Column field="mismatchCount" header="Mismatches" sortable></Column>
                <Column field="pathogenLocation" header="Sample Location" sortable></Column>
                <Column field="pathogenCollectionDate" header="Sample Date" sortable></Column>
                <Column field="pathogenAccessionID" header="Accession ID"></Column>
                <Column field="groupIndex" header="Actions" sortable>
                    <template #body="slotProps">
                        <button class="blue-table-button" @click="changeActiveMismatch(slotProps.data.groupIndex)">View</button>
                    </template>
                </Column>
            </DataTable>
            <div class="mismatch-display-container">
                <div class="mismatch-wrapper">
                    <div class="sequence-wrapper fwdx-seq">
                        <div :class="`sequence-char ${activeMismatch.oligoName.replaceAll(' ', '')}-sequence-char`" v-for="(x, index) in activeMismatch.oligoSequence">{{ x }}</div>
                    </div>
                    <div class="sequence-wrapper mismatch-seq">
                        <div v-for="(x, index) in activeMismatch.mismatchLines" :class="[x=='|' ? 'matchSymbol' : 'mismatchSymbol', `sequence-char ${activeMismatch.oligoName.replaceAll(' ', '')}-sequence-char`]"><span>{{ x }}</span></div>
                    </div>
                    <div class="sequence-wrapper genomic-seq">
                        <div :class="`sequence-char ${activeMismatch.oligoName.replaceAll(' ', '')}-sequence-char`" v-for="(x, index) in activeMismatch.pathogenSequence">{{ x }}</div>
                    </div>
                </div>
                <div class="mismatch-indices">
                    <p>{{ activeMismatch.start_index }}</p>
                    <p>{{ activeMismatch.end_index }}</p>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .mismatch-container {
        width: 100%;
        height: auto;
        border-top: 1.25pt solid var(--light-gray-outline);
        padding-bottom: 1.25em;
        padding-top: 1.25em;
    }

    .mismatch-container:is(:first-of-type) {
        /* padding-top: 1.25em; */
        /* padding-bottom: 2.5em;
        padding-top: 2.5em; */
        /* margin-bottom: 2.5em; */
        /* border-bottom: 1.5pt solid var(--light-gray-outline); */
        /* border-top: 1.5pt solid var(--light-gray-outline); */
    }

    .inline-icon {
        height: var(--body-text-size);
        margin-right: 0.4em;
    }

    .mismatch-title-wrapper{
        height: auto;
        display: flex;
        width: 100%;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
    }

    .mismatch-title-wrapper:hover{
        cursor: pointer;
    }

    .mismatch-title-wrapper:hover > .mismatch-title{
        color: #555555;
    }
    


    .mismatch-title {
        font-size: var(--body-text-size);
        font-weight: 600;
        color: var(--dark-gray-text);
    }

    .mismatch-content-wrapper{
        margin-bottom: 1.25em;
    }

    .mismatch-display-container {
        display: grid;
        grid-template-columns: 100%;
        grid-template-rows: auto 1.5em;
    }

    .mismatch-indices {
        /* background-color: blue; */
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: var(--dark-gray-text);
        font-size: 9pt;
        padding: 0 0.3em;
    }

    .mismatch-wrapper{
        border-radius: 5px;
        width: 100%;
        max-width: 100%;
        overflow-x: scroll;
        border: 2pt solid var(--light-gray-outline);
        height: auto;
    }
    .sequence-wrapper {
        display: flex;
        justify-content: space-between;
        width: 100%;
    }

    .mismatch-seq {
        /* background-color: #f3f3f3; */
        /* height: 1.5em; */
        height: calc(1.5em + 2pt);
    }

    .mismatch-seq > .sequence-char {
        border-top: 1.5pt solid var(--light-gray-outline);
        border-bottom: 1.5pt solid var(--light-gray-outline);
    }

    .matchSymbol > span{
        font-weight: 900;
    }

    .mismatchSymbol > span {
        font-weight: var(--mismatch-body-weight);
    }

    .sequence-char.matchSymbol {
        color: #f3f3f3;
        background-color: var(--green-text);
        font-weight: var(--mismatch-body-weight);
        font-size: 8pt;
    }

    .sequence-char.mismatchSymbol {
        color: #f3f3f3;
        background-color: var(--red-text);
        font-weight: var(--mismatch-body-weight);
    }

    .genomic-seq, .fwdx-seq {
        background-color: white;
        height: 2em;
    }

    .genomic-seq>.sequence-char, .fwdx-seq>.sequence-char{
        background-color: white;
    }

    .fwdx-seq {
        border-top-left-radius: 5px;
        border-radius: 5px 5px 0 0;
    }

    .genomic-seq {
        border-radius: 0 0 5px 5px;
    }

    .sequence-char {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: transparent;
        font-size: var(--body-text-size);
        font-weight: 500;
        height: 100%;
        min-width: 32px;
    }

    .sequence-char:not(:last-child) {
        border-right: 2pt solid var(--light-gray-outline);
    }


</style>