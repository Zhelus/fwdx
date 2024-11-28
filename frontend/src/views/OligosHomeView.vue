<script setup>
import { useRouter } from 'vue-router';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import { ref, onMounted } from 'vue';
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import oligosApi from '@/services/oligosApiHelper';

const router = useRouter();

// State for oligos and loading indicator
const oligos = ref([]);
const loading = ref(false);

function actionClicked(path, oligoId) {
  if (path && oligoId) {
    router.push({ path, query: { id: oligoId } }); // Pass the oligo ID as a query parameter
  } else {
    router.push(path);
  }
}


// Fetch active oligos from the API
async function fetchOligos() {
  loading.value = true;
  try {
    const fetchedOligos = await oligosApi.getActiveOligos();
    // Transform the API response to match the table format
    oligos.value = fetchedOligos.map((oligo) => ({
      id: oligo._id,
      name: oligo.name,
      sequence: oligo.sequence,
      dnaStrandPositive: oligo.dna_strand_positive
    }));
  } catch (error) {
    console.error('Failed to fetch oligos:', error);
  } finally {
    loading.value = false;
  }
}

// Fetch data on component mount
onMounted(() => {
  fetchOligos();
});

// Filters for the table
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
  sequence: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
  dnaStrandPositive: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
});
</script>


<template>
  <div class="oligos-wrapper">
    <div class="header-container">
      <h2 class="page-title">Active Oligos</h2>
      <button class="add-oligo-button" @click="actionClicked('/oligos/add', null)">Add Oligo</button>
    </div>

    <!-- Show loading indicator -->
    <div v-if="loading" class="loading-indicator">Loading...</div>

    <DataTable
      v-else
      :value="oligos"
      :rows="10"
      :rowsPerPageOptions="[5, 10, 15]"
      paginator
      v-model:filters="filters"
      filter-display="menu"
      :globalFilterFields="['name', 'sequence', 'dnaStrandPositive']"
      removableSort
      currentPageReportTemplate="{currentPage} / {totalPages}"
      paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
    >
      <!-- Column Definitions -->
      <Column field="name" header="Oligo Name" sortable>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by oligo name" />
        </template>
      </Column>

      <Column field="sequence" header="Sequence" sortable>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by sequence" />
        </template>
      </Column>

      <Column field="dnaStrandPositive" header="DNA Strand Positive" sortable>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="True/False" />
        </template>
      </Column>

      <!-- Actions Column -->
      <Column header="Actions">
        <template #body="slotProps">
          <div class="action-buttons">
            <button class="action-button" @click="actionClicked('/oligos/view', slotProps.data.id)">View</button>
            <button
              class="action-button delete"
              @click="() => oligosApi.archiveOligo(slotProps.data.id).then(fetchOligos)"
            >
              Archive
            </button>
          </div>
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<style scoped>
.oligos-wrapper {
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

.add-oligo-button {
  background-color: #FFC107;
  color: #000;
  border: none;
  border-radius: 5px;
  padding: 6px 12px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-oligo-button:hover {
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
