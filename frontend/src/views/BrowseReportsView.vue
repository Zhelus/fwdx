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
        const report = new Report(
            "8877665",
            "Test Report 6",
            "9876543",
            "6730f02aec38fbfe063398da",
            "10632",
            "11/17/24",
            ["Mismatch 1", "Mismatch 2"]
        );
        var updatedReportData = {
            'report_title': "Test Report 5 Update",
            'creation_date': "11/18/24"
        }
        reportsApiHelper.updateReport(report.getId(), updatedReportData).catch( error => { console.error(error) } );
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
    <div class="loader" v-if="!initComplete"></div>
    <h1 class="form-header">Browse Reports</h1>
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
        <Column header="Actions">
            <!-- Use to pass custom content to a cell of the data table -->
            <template #body="slotProps">
                <button class="view-report-button">View</button>
            </template>
        </Column>
    </DataTable>
    <button @click="createReport">Create Report</button>
    <button @click="getReport">Get Report</button>
    <button @click="updateReport">Update Report</button>
    <button @click="deleteReport">Delete Report</button>
    <button @click="getAllReports">Get All Reports</button>
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
        font-size: 26pt;
        line-height: 0.95em;
        margin-bottom: 2.5rem;
    }

    .view-report-button {
        background-color: var(--fwdx-blue);
        color: var(--blue-button-text);
        border-radius: 5px;
        height: 25px;
        width: 60%;
        border: none;
        outline: none;
        font-size: 11pt;
        font-weight: 500;
    }

    .view-report-button:hover {
        cursor: pointer;
        background-color: var(--fwdx-blue-button-hover);
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