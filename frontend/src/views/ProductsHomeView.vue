<script setup>
import { useRouter } from 'vue-router';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputText from 'primevue/inputtext';
import { ref, onMounted } from 'vue';
import { FilterMatchMode, FilterOperator } from '@primevue/core/api';
import productsApi from '@/services/productsApiHelper';

const router = useRouter();

// State for products and loading indicator
const products = ref([]);
const loading = ref(false);

function actionClicked(path) {
  router.push(path);
}

// Fetch products from the API
async function fetchProducts() {
  loading.value = true;
  try {
    const fetchedProducts = await productsApi.getAllProductsWithOligoNames();
    // Transform the API response to match the table format
    products.value = fetchedProducts.map((product) => {
      const activeVersionIndex = product.active_version_index;
      const activeVersionOligos = product.versions[activeVersionIndex] || [];
      return {
        id: product._id,
        productName: product.name,
        activeVersion: activeVersionIndex + 1, // Convert to 1-based index
        versions: product.versions.length,
        oligoNames: activeVersionOligos, // Pass full oligo details, including 'archived'
      };
    });

  } catch (error) {
    console.error('Failed to fetch products:', error);
  } finally {
    loading.value = false;
  }
}

// Fetch data on component mount
onMounted(() => {
  fetchProducts();
});

// Filters for the table
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  productName: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
  activeVersion: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
  versions: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] },
  oligoNamesString: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.CONTAINS }] },
});
</script>

<template>
  <div class="products-wrapper">
    <div class="header-container">
      <h2 class="page-title">Products</h2>
      <button class="add-product-button" @click="actionClicked('/reagents/add', null)">Add Product</button>
    </div>

    <!-- Show loading indicator -->
    <div v-if="loading" class="loading-indicator">Loading...</div>

    <DataTable v-else :value="products" :rows="10" :rowsPerPageOptions="[5, 10, 15]" paginator v-model:filters="filters"
      filter-display="menu" :globalFilterFields="['productName', 'activeVersion', 'versions', 'numberOfOligos']"
      removableSort currentPageReportTemplate="{currentPage} / {totalPages}"
      paginatorTemplate="FirstPageLink PrevPageLink CurrentPageReport NextPageLink LastPageLink">
      <!-- Column Definitions -->
      <Column field="productName" header="Product Name" sortable>
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by product name" />
        </template>
      </Column>

      <Column field="activeVersion" header="Active Version" sortable dataType="numeric">
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by version" />
        </template>
      </Column>

      <Column field="versions" header="Number of Versions" sortable dataType="numeric">
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by versions" />
        </template>
      </Column>

      <!-- Oligo Names Column -->
      <Column field="oligoNamesString" header="Oligo Names">
        <template #filter="{ filterModel }">
          <InputText v-model="filterModel.value" placeholder="Search by oligo names" />
        </template>
        <template #body="slotProps">
          <ul>
            <li v-for="(oligo, index) in slotProps.data.oligoNames" :key="index"
              :style="{ color: oligo.archived ? 'red' : 'inherit' }">
              {{ oligo.name }}
            </li>
          </ul>
        </template>
      </Column>
      <!-- Actions Column -->
      <Column header="Actions">
        <template #body="slotProps">
          <div class="action-buttons">
            <button class="action-button" @click="actionClicked(`/reagents/view/${slotProps.data.id}`)">
              View
            </button>
            <button class="action-button edit" @click="actionClicked('/products/edit', slotProps.data.productName)">
              Edit
            </button>
          </div>
        </template>
      </Column>
    </DataTable>
  </div>
</template>

<style scoped>
.products-wrapper {
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

.action-button.edit {
  background-color: #1A1A3A;
  color: #FFF;
}

.action-button.edit:hover {
  background-color: #14122b;
}
</style>
