<template>
    <div class="pathogen-detail-wrapper">
        <div class="header-container">
            <h2 class="page-title">{{ pageTitle }}</h2>
            <button class="back-button" @click="goBack">Back</button>
        </div>

        <!-- Show loading indicator -->
        <div v-if="loading" class="loading-indicator">Loading...</div>

        <!-- DataTable to show pathogen details -->
        <DataTable
            v-else
            :value="pathogenDetails"
            :rows="10"
            :rowsPerPageOptions="[5, 10, 15]"
            paginator
            removableSort
        >
            <!-- Column Definitions -->
            <Column field="accessID" header="Pathogen ID" sortable />
            <Column field="isolate" header="Isolate" sortable />
            <Column field="length" header="Completeness" sortable />
            <Column field="collectionDate" header="Collection Date" sortable />
            <Column field="locationName" header="Sample Origin" sortable />


        </DataTable>
    </div>
</template>

<script setup>
import { useRoute,useRouter } from 'vue-router';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import { ref, onMounted } from 'vue';
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import pathogensApi from '@/services/pathogensApiHelper'; // Updated service import
// Router and state variables
const route = useRoute(); // Use `useRoute` to access query parameters
const router = useRouter();
const pathogenDetails = ref(null);
const loading = ref(true);
const pageTitle = ref(''); // Correctly declare pageTitle as a reactive variable

// Fetch pathogen details
async function fetchPathogenDetails(taxonomicID) {
    try {
        console.log("Fetching details for taxonomicID:", taxonomicID);
        const fetchedDetails = await pathogensApi.getPathogenByTaxonomicID(taxonomicID);

        if (!fetchedDetails || !fetchedDetails.length) {
            console.error("No details found for taxonomicID:", taxonomicID);
            pathogenDetails.value = [];
        } else {
            console.log("Fetched Pathogen Details:", fetchedDetails);

            // Avoid directly modifying reactive dependencies
            const transformedDetails = fetchedDetails.map((pathogen) => ({
                accessID: pathogen.accessionID,
                //commonName: pathogenDetails.common_name || 'N/A',
                collectionDate: pathogen.collection_date || 'Unavailable',
                isolate: pathogen.isolate || 'Unavailable',
                locationName: pathogen.geo_loc_name || 'Unavailable',
                length: pathogen.sequence_length || 'Unknown'

            }));

            pathogenDetails.value = Object.freeze(transformedDetails); // Use frozen data
        }
    } catch (error) {
        console.error("Error fetching pathogen details:", error);
        pathogenDetails.value = [];
    } finally {
        loading.value = false;
    }
}

// Go back to the previous page
function goBack() {
    router.back();
}

// Fetch data on component mount
onMounted(() => {
    const taxonomicID = route.query.id; // Get taxonomicID from query params
    const commonName = route.query.name; // Get common name from query params
    if (taxonomicID) {
        fetchPathogenDetails(taxonomicID);
    } else {
        console.error("Taxonomic ID is missing in the route.");
        loading.value = false;
    }
    pageTitle.value = commonName || 'Pathogen Details';
});
</script>

<style scoped>
.pathogen-detail-wrapper {
    padding: 2rem;
    background-color: #f8f9fa;
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.header-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.page-title {
    font-size: 24px;
    font-weight: bold;
    color: var(--fwdx-blue);
}

.back-button {
    background-color: #FFC107;
    color: #000;
    border: none;
    border-radius: 5px;
    padding: 6px 12px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s;
}

.back-button:hover {
    background-color: #e0a800;
}

.loading-indicator {
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #007bff;
}

.error-message {
    text-align: center;
    color: red;
    font-size: 16px;
}

.detail-table table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
}

.detail-table th,
.detail-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.detail-table th {
    background-color: #f4f4f4;
    font-weight: bold;
}
</style>