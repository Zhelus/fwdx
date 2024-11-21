<!-- 
Page view for browsing reports
Last edited by: Blake Good
Date: 11/11/24
-->
<script setup>
    import DataTable from 'primevue/datatable';
    import Column from 'primevue/column';
    import { InputText } from 'primevue';
    import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
    import { ref } from 'vue';
    import reportsApiHelper from "@/services/reportsApiHelper"
    import Report from "@/entities/Report"
    import { onBeforeMount } from 'vue';
    import LoadingIcon from '@/components/misc/LoadingIcon.vue';
    import ViewReportButton from '@/components/misc/ViewReportButton.vue';

    // Work to be done before the page is displayed
    // We only show the table after all reports are fetched (initComplete = true)
    const initComplete = ref(false);
    const reports = ref([]);
    onBeforeMount(async () => {
        // GET all reports from MongoDB
        await reportsApiHelper.getAllReports()
                .then(data => {
                    reports.value = data;
                    for(let i=0; i<reports.value.length; i++){
                        reports.value[i]['mismatchCount'] = reports.value[i]['mismatches'].length;
                    }
                }).catch(error => {
                    console.error(error);
                });
        // Show the table with report data
        setTimeout(() => {
            initComplete.value = true;
        }, "1000")
    })
    
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
        pathogen_id: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        reagent_id: { 
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
    <h1 class="form-header">All Reports</h1>
    <!-- Use to add a new data table component to the page -->
    <DataTable 
        v-if="initComplete"
        :value="reports"  
        :rows="10" :rowsPerPageOptions="[5, 10, 15, 20]"
        paginator
        paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
        currentPageReportTemplate="{currentPage} / {totalPages}"
        v-model:filters="filters"
        filter-display="menu"
        :globalFilterFields="['title', 'pathogen', 'reagent', 'sourceDB']"
        removableSort
    >
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
        <Column field="pathogen_id" header="Pathogen" sortable>
            <template #filter="{ filterModel }">
                <InputText
                v-model="filterModel.value"
                type="text"
                placeholder="Search by pathogen"/>
             </template> 
        </Column>
        <Column field="reagent_id" header="Reagent" sortable>
            <template #filter="{ filterModel }">
                <InputText
                v-model="filterModel.value"
                type="text"
                placeholder="Search by reagent"/>
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
        <Column field="report_id" header="Actions">
            <!-- Use to pass custom content to a cell of the data table -->
            <template #body="slotProps">
                 <ViewReportButton button-class="table-button" :report-id="slotProps.data.report_id" />
            </template>
        </Column>
    </DataTable>
    <!-- <button @click="updateReport()">Update Mismatches</button> -->
</div>
</template>
<style scoped>
    .browse-reports-wrapper {
        min-height: 100%;
        height: 100%;
        max-height: 100%;
        background-color: var(--gray-page-background);
        padding: 2rem;
        min-width: 100%;
    }

    .form-header {
        color: var(--fwdx-blue);
        font-weight: 700;
        vertical-align:top;
        letter-spacing: -2%;
        font-size: var(--page-header-size);
        line-height: 0.95em;
        margin-bottom: 1rem;
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