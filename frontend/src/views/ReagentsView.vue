<script setup>
import { useRouter } from 'vue-router';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import { ref } from 'vue';
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';

const router = useRouter();

function actionClicked(path, productName) {
  if (path && productName) {
    router.push({ path, query: { productName } });
  }
}

// Sample data for the table with Active Version
const reagents = [
  { id: 1, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #001", activeVersion: 1, numberOfOligos: 3 },
  { id: 2, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #002", activeVersion: 2, numberOfOligos: 6 },
  { id: 3, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #003", activeVersion: 3, numberOfOligos: 7 },
  { id: 4, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #004", activeVersion: 2, numberOfOligos: 5 },
  { id: 5, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #005", activeVersion: 1, numberOfOligos: 3 },
  { id: 6, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #006", activeVersion: 4, numberOfOligos: 4 },
];

const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  taxonomicName: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
  productName: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
  activeVersion: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
  numberOfOligos: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
});
</script>

<template>
  <div class="reagents-wrapper">
    <div class="header-container">
      <h2 class="page-title">Reagents</h2>
      <button class="add-product-button" @click="actionClicked('/reagents/add')">Add Reagent Product</button>
    </div>

    <DataTable 
      :value="reagents"  
      :rows="10" 
      :rowsPerPageOptions="[5, 10, 15]"
      paginator
      v-model:filters="filters"
      filter-display="menu"
      :globalFilterFields="['taxonomicName', 'productName', 'activeVersion']"
      removableSort
      currentPageReportTemplate="{currentPage} / {totalPages}"
      paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink"
    >
      <!-- Column Definitions -->
      <Column field="taxonomicName" header="Taxonomic Name" sortable>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by taxonomic name"/>
        </template>
      </Column>
      
      <Column field="productName" header="Product Name" sortable>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by product name"/>
        </template>
      </Column>

      <Column field="activeVersion" header="Active Version" sortable dataType="numeric">
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by version"/>
        </template>
      </Column>
      
      <Column field="numberOfOligos" header="Number of Oligos" sortable dataType="numeric">
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by oligos"/>
        </template>
      </Column>

      <!-- Actions Column with Buttons -->
      <Column header="Actions">
        <template #body="slotProps">
          <div class="action-buttons">
          <button class="action-button" @click="actionClicked('/reagents/add', slotProps.data.productName)">Add</button>
          <button class="action-button edit" @click="actionClicked('/reagents/edit', slotProps.data.productName)">Edit</button>
        </div>
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<style scoped>
.reagents-wrapper {
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

.add-product-button {
  background-color: #FFC107;
  color: #000;
  border: none;
  border-radius: 5px;
  padding: 6px 12px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-product-button:hover {
  background-color: #e0a800;
}

/* Style for the action buttons container to add space */
.action-buttons {
  display: flex;
  gap: 10px; /* Space between Add and Edit buttons */
}

.action-button {
  background-color: #FFC107;
  color: #000;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  padding: 8px 20px; /* Broader button width */
  transition: background-color 0.3s;
  width: 100px; /* Set a fixed width for both buttons */
}


.action-button:hover {
  background-color: #e0a800;
}

.action-button.edit {
  background-color: #1A1A3A;
  color: #FFF;
}

.action-button.edit:hover {
  background-color: #14122b;
}
</style>
