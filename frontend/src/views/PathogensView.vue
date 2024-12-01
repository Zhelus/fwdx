<template>
    <div class="pathogens-wrapper">
        <div class="header-container">
            <h2 class="page-title">Pathogens</h2>
            <button class="add-pathogen-button" @click="actionClicked('/pathogens/add', null)">Add Pathogen</button>
        </div>

        <!-- Show loading indicator -->
        <div v-if="loading" class="loading-indicator">Loading...</div>

        <DataTable
            v-else
            :value="pathogens"
            :rows="10"
            :rowsPerPageOptions="[5, 10, 15]"
            paginator
            :filters="filters"
            filter-display="menu"
            :globalFilterFields="['taxonomicID', 'commonName', 'countTotal']"
            removableSort
        >
        <!-- Column Definitions -->
        <Column field="taxonomicID" header="Taxonomic ID" sortable>
            <template #filter="{ filterModel }">
                <InputText v-model="filterModel.value" placeholder="Search by Taxonomic ID" />
            </template>
        </Column>

        <Column field="commonName" header="Common Name" sortable>
            <template #filter="{ filterModel }">
                <InputText v-model="filterModel.value" placeholder="Search by Common Name" />
            </template>
        </Column>

        <Column field="countTotal" header="Cached Sequences" sortable>
            <template #filter="{ filterModel }">
                <InputText v-model="filterModel.value" placeholder="NA" />
            </template>
        </Column>

        <Column field="variants" header="Variants" sortable>
            <template #filter="{ filterModel }">
                <InputText v-model="filterModel.value" placeholder="NA" />
            </template>
        </Column>

        <!-- Actions Column -->
        <Column header="Actions">
            <template #body="slotProps">
                <div class="action-buttons">
                    <button
                        class="action-button"
                        @click="actionClicked('/pathogens/view', slotProps.data.taxonomicID, slotProps.data.commonName)"
                    >
                        View
                    </button>
                </div>
            </template>
        </Column>
        </DataTable>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import { ref, onMounted } from 'vue';
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import pathogensApi from '@/services/pathogensApiHelper'; // Updated service import

const router = useRouter();

// State for pathogens and loading indicator
const pathogens = ref([]);
const loading = ref(false);

// Fetch pathogens from the API
async function fetchPathogens() {
    loading.value = true;
    try {
        const fetchedPathogens = await pathogensApi.getAllPathogens();
        
        if (Array.isArray(fetchedPathogens.pathogens)) {
            pathogens.value = fetchedPathogens.pathogens.map((pathogen) => ({
                taxonomicID: pathogen.taxonomicID,
                commonName: pathogen.common_name,
                countTotal: pathogen.count,
//                variants: pathogen.variant_count 
            }));
        } else {
            console.error("Unexpected API response format:", fetchedPathogens);
        }

        /*
        console.log("Transformed Pathogens for Table:", fetchedPathogens);
        // Transform the API response to match the table format
        pathogens.value = fetchedPathogens.map((pathogen) => ({
            taxonomicID: pathogen.taxonomicID,
            commonName: pathogen.common_name,
            countTotal: pathogen.count,
        }));
        console.log("Transformed Pathogens for Table:", pathogens.value);
        */

//        totalRecords.value = fetchedPathogens.length;
    } catch (error) {
        console.error('Failed to fetch pathogens:', error);
    } finally {
        loading.value = false;
    }
}
/*
function actionClicked(path, taxonomicID) {
    if (path && taxonomicID) {
        router.push({ path, query: { id: taxonomicID } });
    } else {
        console.error("Invalid path or taxonomicID");
    }
}
*/    
function actionClicked(path, taxonomicID, commonName) {
    if (path && taxonomicID && commonName) {
        router.push({ path, query: { id: taxonomicID, name: commonName} });
    } else {
        router.push(path);
    }
}


// Fetch data on component mount
onMounted(() => {
    fetchPathogens();
});

// Filters for the table
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    taxonomicID: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    commonName: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    countTotal: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
    variants: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
});
</script>

<style scoped>
.pathogens-wrapper {
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

.add-pathogen-button {
    background-color: #FFC107;
    color: #000;
    border: none;
    border-radius: 5px;
    padding: 6px 12px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s;
}

.add-pathogen-button:hover {
    background-color: #e0a800;
}

.loading-indicator {
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #007bff;
}

.action-buttons {
    display: flex;
    gap: 10px;
}

.action-button {
    background-color: #FFC107;
    color: #000;
    border: none;
    border-radius: 5px;
    font-weight: bold;
    cursor: pointer;
    padding: 8px 20px;
    transition: background-color 0.3s;
    width: 100px;
}

.action-button:hover {
    background-color: #e0a800;
}

.action-button.delete {
    background-color: #dc3545;
    color: #FFF;
}

.action-button.delete:hover {
    background-color: #a71d2a;
}
</style>