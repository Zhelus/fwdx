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
    import api from "@/services/apiClient.js";
    import reportsApiHelper from "@/services/reportsApiHelper"
    import Report from "@/entities/Report"
    const search = ref("")



    // Test data for the reports data table
    const reports = [
        {
            title: 'Report 1',
            date: '11/2/24 @ 10:30am',
            pathogen: 'Candida Auris',
            reagent: 'Reagent 1',
            sourceDB: 'NCBI',
            mismatchCount: '2'
        },
        {
            title: 'Report 2',
            date: '11/1/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 2',
            sourceDB: 'NCBI',
            mismatchCount: '6'
        },
        {
            title: 'Report 3',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 5',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 1',
            date: '11/2/24 @ 10:30am',
            pathogen: 'Candida Auris',
            reagent: 'Reagent 1',
            sourceDB: 'NCBI',
            mismatchCount: '2'
        },
        {
            title: 'Report 2',
            date: '11/1/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 2',
            sourceDB: 'NCBI',
            mismatchCount: '6'
        },
        {
            title: 'Report 3',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 5',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 2',
            date: '11/1/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 2',
            sourceDB: 'NCBI',
            mismatchCount: '6'
        },
        {
            title: 'Report 3',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 5',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 2',
            date: '11/1/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 2',
            sourceDB: 'NCBI',
            mismatchCount: '6'
        },
        {
            title: 'Report 3',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 5',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 2',
            date: '11/1/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 2',
            sourceDB: 'NCBI',
            mismatchCount: '6'
        },
        {
            title: 'Report 3',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Influenza',
            reagent: 'Reagent 5',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        },
        {
            title: 'Report 4',
            date: '10/31/24 @ 10:30am',
            pathogen: 'Covid-19',
            reagent: 'Reagent 3',
            sourceDB: 'NCBI',
            mismatchCount: '0'
        }
    ]
    
    // JSON object containing the definitions for filters related to the data table
    const filters = ref();
    filters.value = {
        global: { value: null, matchMode: FilterMatchMode.CONTAINS },
        title: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        pathogen: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        reagent: { 
            operator: FilterOperator.AND, 
            constraints: [{ 
                value: null, 
                matchMode: FilterMatchMode.STARTS_WITH 
            }] 
        },
        sourceDB: { 
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
        reportsApiHelper.getReport("1234567")
            .then(data => {
                search.value = data;
            }).catch(error => {
                console.log(error);
            });
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
        reportsApiHelper.saveNewReport(report)
            .then(data => {
                search.value = data;
                console.log(search.value);
            })
            .catch(error => {
                console.error(error);
            })
        // search.value = report.saveNewReport();
    }

    // Update a single report with new data
    function updateReport(){
        const report = new Report(
            "1133557",
            "Test Report 5",
            "9876543",
            "6730f02aec38fbfe063398da",
            "10632",
            "11/17/24",
            ["Mismatch 1", "Mismatch 2"]
        );
        var updatedReportData = {
            'report_title': "Test Report Update 2",
            'creation_date': "11/10/24"
        }
        search.value = report.updateReport(updatedReportData);
    }

    // Delete a single report 
    function deleteReport(){
        const report = new Report(
            "1133557",
            "Test Report Update 2",
            "9876543",
            "6730f02aec38fbfe063398da",
            "10632",
            "11/10/24",
            ["Mismatch 1", "Mismatch 2"]
        );
        search.value = report.deleteReport();
    }

    function getAllReports() {
        reportsApiHelper.getAllReports()
            .then(data => {
                search.value = data;
            })
            .catch(error => {
                console.error(error);
            });
    }

</script>
<template>
<div class="browse-reports-wrapper">
    <h1 class="form-header">Browse Reports</h1>
    <!-- Use to add a new data table component to the page -->
    <DataTable 
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
        <Column field="title" header="Title" sortable>
            <!-- Use to add a filter element to a column in the table  -->
            <template #filter="{ filterModel }">
                <InputText
                v-model="filterModel.value"
                type="text"
                placeholder="Search by title"/>
             </template> 
        </Column>
        <Column field="date" header="Date" sortable></Column>
        <Column field="pathogen" header="Pathogen" sortable>
            <template #filter="{ filterModel }">
                <InputText
                v-model="filterModel.value"
                type="text"
                placeholder="Search by pathogen"/>
             </template> 
        </Column>
        <Column field="reagent" header="Reagent" sortable>
            <template #filter="{ filterModel }">
                <InputText
                v-model="filterModel.value"
                type="text"
                placeholder="Search by reagent"/>
             </template> 
        </Column>
        <Column field="sourceDB" header="Source DB" sortable>
            <template #filter="{ filterModel }">
                <InputText
                v-model="filterModel.value"
                type="text"
                placeholder="Search by source database"/>
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


    <p class="reports-p">The Report Is: {{ search }}</p>
</div>
</template>
<style scoped>
    .reports-p {
        visibility: visible;
        display: block;
        font-size: 12pt;
        color: black;
    }
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
</style>