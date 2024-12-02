<!-- 
Page view for browsing reports
Last edited by: Blake Good
Date: 11/11/24
-->
<script setup>
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import { InputText, IconField, InputIcon } from 'primevue';
    import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
    import { ref } from 'vue';
    import reportsApiHelper from "@/services/reportsApiHelper"
    import Report from "@/entities/Report"
    import { onBeforeMount, onMounted, onUpdated } from 'vue';
    import LoadingIcon from '@/components/misc/LoadingIcon.vue';
    import ViewReportButton from '@/components/misc/ViewReportButton.vue';
    import BackButton from '@/components/misc/BackButton.vue';
    import { filter } from '@primeuix/utils';

    // Work to be done before the page is displayed
    // We only show the table after all reports are fetched (initComplete = true)
    const initComplete = ref(false);
    const reports = ref([]);
    const filterButtons = ref();
    const keyOrder = ['report_title', 'pathogen_name', 'product_name', 'mismatchCount'];
    onBeforeMount(async () => {
        // GET all reports from MongoDB
        await reportsApiHelper.getAllReports()
                .then(data => {
                    console.log(data);
                    reports.value = data;
                    for(let i=0; i<reports.value.length; i++){
                        reports.value[i]['mismatchCount'] = reports.value[i]['mismatches'].length;
                    }
                    initComplete.value = true;

                }).catch(error => {
                    console.error(error);
                });
        // reports.value = [
        //     {"_id":{"$oid":"673136062c3c0e7613ca1b9a"},
        //     "report_id":"1234567",
        //     "schedule_id":"7654321",
        //     "report_title":"Test Report 1",
        //     "reagent_id":"6730f02aec38fbfe063398da",
        //     "pathogen_name":"10632",
        //     "mismatches":[{"oligoID":"67366cb26b5f81586e616809","oligoName":"Forward Primer","oligoSequence":"AATGCAACAGTGCAATCTCA","mismatchLines":"|||||X||||||||||||||","pathogenSequence":"AATGCCACAGTGCAATCTCA","pathogenAccessionID":"KJ643523.1","pathogenCommonName":"Respiratory syncytial virus type A","pathogenCollectionDate":"2015","pathogenLocation":"USA","genomicPosition":"1987","mismatchIndex":["5"],"mismatchCount":"1"},{"oligoID":"67366cb26b5f81586e616809","oligoName":"Reverse Primer","oligoSequence":"GGCCCAACACCAAATTCATC","mismatchLines":"||||XX||X||XX|XX|||X","pathogenSequence":"GGCCTTACTCCTGAAACATA","pathogenAccessionID":"MF001052.1","pathogenCommonName":"Respiratory syncytial virus type A","pathogenCollectionDate":"2015","pathogenLocation":"USA","genomicPosition":"708","mismatchIndex":["4", "5", "8","11","12","14","15", "19"],"mismatchCount":{"$numberInt":"8"}},{"oligoID":"67366cb26b5f81586e616809","oligoName":"Probe 1","oligoSequence":"AAACCTGCTTAGTTTCTTCTTGTTCTC","mismatchLines":"||||||||||||||||||||X|||||X","pathogenSequence":"AAACCTGCTTAGTTTCTTCTGGTTCTT","pathogenAccessionID":"MG027862.1","pathogenCommonName":"Respiratory syncytial virus type A","pathogenCollectionDate":"2015","pathogenLocation":"USA","genomicPosition":"3861","mismatchIndex":[{"$numberInt":"21"},{"$numberInt":"27"}],"mismatchCount":{"$numberInt":"2"}}],
        //     "creation_date":"11/15/24"}
        // ]
        initComplete.value = true;
    })

    onMounted(() => {
        filterButtons.value = document.getElementsByClassName("p-datatable-column-filter-button");
    });

    onUpdated(() => {
        // Chang the color of the filter icons when a filter is applied
        console.log("UPDATED")
        for(let i=0; i<keyOrder.length; i++){
            if(filters.value[keyOrder[i]].constraints[0].value !== null){
                filterButtons.value[i].classList.add("in-use");
                console.log("ADDING");
            }
            else{
                filterButtons.value[i].classList.remove("in-use");
                console.log("NOT ADDING");   
            }
        }
    });
    
    // JSON object containing the definitions for filters related to the data table
    const filters = ref();
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        report_title: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        pathogen_name: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        product_name: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        mismatchCount: { 
            operator: FilterOperator.AND, 
            constraints: [{
                value: null, 
                matchMode: FilterMatchMode.EQUALS 
            }] 
        }
    };

    // Get a single report from MongoDB using the report's ID
    function getReport(){
        reportsApiHelper.getReport("1234567").catch( error => { console.error(error) } );
    }

    // Create a new report and send it to the backend
    function createReport(){
        const report = new Report(
            "9393939",
            "Test Report 7",
            "9876543",
            "6730f02aec38fbfe063398da",
            "10632",
            "11/18/24",
            ["Mismatch 1", "Mismatch 2"]
        )
        reportsApiHelper.saveNewReport(report).catch( error => { console.error(error) } );
    }

    // Update a single report with new data
    function updateReport(){
        var updatedReportData = {
            'mismatches': [
                {
                    oligoID: '67366cb26b5f81586e616809',
                    oligoName: "Forward Primer",
                    oligoSequence: 'AATGCAACAGTGCAATCTCA',
                    mismatchLines: '|||||X||||||||||||||',
                    pathogenSequence: 'AATGCCACAGTGCAATCTCA',
                    pathogenAccessionID: 'KJ643523.1',
                    pathogenCommonName: 'Respiratory syncytial virus type A',
                    pathogenCollectionDate: '2015',
                    pathogenLocation: 'USA',
                    genomicPosition: '1987',
                    mismatchIndex: [5],
                    mismatchCount: 1
                },
                {
                    oligoID: '67366cb26b5f81586e616809',
                    oligoName: "Reverse Primer",
                    oligoSequence: 'GGCCCAACACCAAATTCATC',
                    mismatchLines: '||||XX||X||XX|XX|||X',
                    pathogenSequence: 'GGCCTTACTCCTGAAACATA',
                    pathogenAccessionID: 'MF001052.1',
                    pathogenCommonName: 'Respiratory syncytial virus type A',
                    pathogenCollectionDate: '2015',
                    pathogenLocation: 'USA',
                    genomicPosition: '708',
                    mismatchIndex: [4, 5, 8, 11, 12, 14, 15, 19],
                    mismatchCount: 8
                },
                {
                    oligoID: '67366cb26b5f81586e616809',
                    oligoName: "Probe 1",
                    oligoSequence: 'AAACCTGCTTAGTTTCTTCTTGTTCTC',
                    mismatchLines: '||||||||||||||||||||X|||||X',
                    pathogenSequence: 'AAACCTGCTTAGTTTCTTCTGGTTCTT',
                    pathogenAccessionID: 'MG027862.1',
                    pathogenCommonName: 'Respiratory syncytial virus type A',
                    pathogenCollectionDate: '2015',
                    pathogenLocation: 'USA',
                    genomicPosition: '3861',
                    mismatchIndex: [21, 27],
                    mismatchCount: 2
                }
            ]
        }
        reportsApiHelper.updateReport('1234567', updatedReportData).catch( error => { console.error(error) } );
    }

    // Delete a single report 
    function deleteReport(){
        const report = new Report(
            "9393939",
            "Test Report Update 7",
            "9876543",
            "6730f02aec38fbfe063398da",
            "10632",
            "11/18/24",
            ["Mismatch 1", "Mismatch 2"]
        );
        reportsApiHelper.deleteReport(report.getId()).catch( error => { console.error(error) } );
    }

    // Get all reports from the 'Reports' collection
    function getAllReports() {
        reportsApiHelper.getAllReports().catch( error => { console.error(error) } );
    }

</script>
<template>
<div class="browse-reports-wrapper">
    <!-- <div class="loader" v-if="!initComplete"></div> -->
    <LoadingIcon :init-complete="initComplete" />
    <!-- <h1 class="form-header">All Reports</h1> -->
    <!-- Use to add a new data table component to the page -->
    <!-- <Transition> -->
    <BackButton :return-url="'/reports'" :display-warning="false"/>
        <DataTable 
            v-if="initComplete"
            :value="reports"  
            :rows="10" :rowsPerPageOptions="[5, 10, 15, 20]"
            paginator
            paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
            currentPageReportTemplate="{currentPage} / {totalPages}"
            v-model:filters="filters"
            filter-display="menu"
            :globalFilterFields="['report_title', 'pathogen_name', 'product_name', 'creation_date', 'mismatch_count']"
            class="browse-reports-table"
            removableSort
        >
            <template #header>
                <div class="table-search-header">
                <h1 class="form-header">All Reports</h1>
                    <IconField>
                        <!-- <InputIcon>
                            <i class="pi pi-search" />
                        </InputIcon> -->
                        <div class="keyword-search-icon">
                            <img class="iconfield-icon" src="../components/icons/magnifying-glass-icon.svg"></img>
                        </div>
                        <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                    </IconField>
                </div>
            </template>
            <!-- 
                Use to add a new column to the data table 
                - The "sortable" option will allow the column to be sorted
                - The "field" option defines which field/key from the data will be stored in this column
                - The "header" option defines what the name of the column will be displayed as
            -->
            <Column field="report_title" header="Title" sortable>
                <!-- Use to add a filter element to a column in the table  -->
                <template #filter="{ filterModel }">
                    <InputText
                    v-model="filterModel.value"
                    type="text"
                    placeholder="Search by title"/>
                </template> 
            </Column>
            <Column field="creation_date" header="Date" sortable></Column>
            <Column field="pathogen_name" header="Pathogen" sortable>
                <template #filter="{ filterModel }">
                    <InputText
                    v-model="filterModel.value"
                    type="text"
                    placeholder="Search by pathogen"/>
                </template> 
            </Column>
            <Column field="product_name" header="Reagent" sortable>
                <template #filter="{ filterModel }">
                    <InputText
                    v-model="filterModel.value"
                    type="text"
                    placeholder="Search by product"/>
                </template> 
            </Column>
            <!-- Options for a column that is to be filtered numerically  -->
            <Column field="mismatchCount" filterField="mismatchCount" dataType="numeric" header="Mismatches" sortable>
                <template #filter="{ filterModel }">
                    <InputText
                    v-model="filterModel.value"
                    type="text"
                    placeholder="Search by mismatches"/>
                </template> 
            </Column>
            <Column field="_id" header="Actions">
                <!-- Use to pass custom content to a cell of the data table -->
                <template #body="slotProps">
                    <ViewReportButton button-class="table-button" :report-id="slotProps.data._id" />
                </template>
            </Column>
        </DataTable>
    <!-- </Transition> -->
    <!-- <button @click="updateReport()">Update Mismatches</button> -->
</div>
</template>
<style scoped>
    .v-enter-active{
        transition: opacity 0.5s ease;
    }

    .v-leave-active {
        transition: opacity 0.05s ease;
    }

    .v-enter-from, .v-leave-to {
        opacity: 0;
    }

    .browse-reports-wrapper {
        min-height: 100%;
        height: 100%;
        max-height: 100%;
        background-color: var(--gray-page-background);
        padding: 1em 2rem 2rem;
        min-width: 100%;
    }

    .form-header {
        color: var(--fwdx-blue);
        font-weight: 700;
        vertical-align:top;
        letter-spacing: -2%;
        font-size: var(--page-header-size);
        line-height: 0.95em;
        padding-left: 0.9rem;
        /* margin-bottom: 1rem; */
    }

    .loader {
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -120px;
        margin-left: -60px;
        border: 16px solid var(--light-gray-outline);
        border-top: 16px solid var(--fwdx-yellow);
        border-radius: 50%;
        width: 120px;
        height: 120px;
        animation: spin 0.75s ease-in-out infinite, changeColor 1.5s ease-in-out 0s infinite ;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes changeColor {
        0%     {
            /* background-color: var(--fwdx-yellow); */
            border-top: 16px solid var(--fwdx-blue); /* Blue */
        }
        50%  {
            /* background-color:var(--fwdx-white); */
            border-top: 16px solid var(--fwdx-yellow); /* Blue */
        }
        75%  {
            /* background-color:var(--fwdx-white); */
            border-top: 16px solid var(--fwdx-yellow); /* Blue */
        }
        100%{
            border-top: 16px solid var(--fwdx-blue); /* Blue */
        }
    }
</style>