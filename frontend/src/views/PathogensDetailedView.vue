<template>
    <div class="pathogen-detail-wrapper">
        <div class="header-container">
            <h2 class="page-title">Pathogen Details</h2>
            <button class="back-button" @click="goBack">Back</button>
        </div>

        <!-- Show loading indicator -->
        <div v-if="loading" class="loading-indicator">Loading...</div>

        <!-- Show error message if no data -->
        <div v-else-if="!pathogenDetails">
            <p class="error-message">No details found for the selected pathogen.</p>
        </div>

        <!-- Show the table -->
        <div v-else class="detail-table">
            <table>
                <thead>
                    <tr>
                        <th>Field</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Common Name</td>
                        <td>{{ pathogenDetails.common_name }}</td>
                    </tr>
                    <tr>
                        <td>Accession ID</td>
                        <td>{{ pathogenDetails.accessionID }}</td>
                    </tr>
                    <tr>
                        <td>Collection Date</td>
                        <td>{{ pathogenDetails.collection_date }}</td>
                    </tr>
                    <tr>
                        <td>Isolate</td>
                        <td>{{ pathogenDetails.isolate }}</td>
                    </tr>
                    <tr>
                        <td>Geo Location Name</td>
                        <td>{{ pathogenDetails.geo_loc_name }}</td>
                    </tr>
                    <tr>
                        <td>Sequence Length</td>
                        <td>{{ pathogenDetails.sequence_length }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import pathogensApi from '@/services/pathogensApiHelper';

// Router and state variables
const route = useRoute();
const router = useRouter();
const pathogenDetails = ref(null);
const loading = ref(true);

// Fetch pathogen details
async function fetchPathogenDetails(taxonomicID) {
    try {
        console.log("Fetching details for taxonomicID:", taxonomicID);
        const fetchedDetails = await pathogensApi.getPathogenByTaxonomicID(taxonomicID);
        console.log("Fetched Pathogen Details:", fetchedDetails);
        pathogenDetails.value = fetchedDetails;
    } catch (error) {
        console.error("Error fetching pathogen details:", error);
        pathogenDetails.value = null;
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
    if (taxonomicID) {
        fetchPathogenDetails(taxonomicID);
    } else {
        console.error("Taxonomic ID is missing in the route.");
        loading.value = false;
    }
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