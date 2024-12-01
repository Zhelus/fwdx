<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import oligosApi from '@/services/oligosApiHelper';
import productsApi from '@/services/productsApiHelper';
import FormActionButton from '@/components/report_form/FormActionButton.vue';
import FormCheckboxItem from './EditProductFormCheckBoxItem.vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';

const router = useRouter();
const route = useRoute();
const productId = route.params.productId || route.query.id;

// Bindings for the form
const productName = ref('');
const oligos = ref([]);
const selectedOligos = ref([]);
const confirmationText = ref('');

// Fetch data when the component is mounted
onMounted(() => {
  fetchData();
});

async function fetchData() {
  try {
    // Fetch active oligos
    const activeOligos = await oligosApi.getActiveOligos();
    const oligoMap = activeOligos.reduce((map, oligo) => {
      map[oligo._id] = oligo;
      return map;
    }, {});

    // Fetch existing product data
    const productData = await productsApi.getProductById(productId);
    productName.value = productData.name;

    // Get oligos from the active version
    const activeVersionIndex = productData.active_version_index;
    const activeVersionOligos = productData.versions[activeVersionIndex] || [];

    // Extract the oligo IDs from the active version
    const activeVersionOligoIds = activeVersionOligos.map(oligo => oligo._id);

    // Add archived oligos from active version to oligoMap if they are not already included
    activeVersionOligos.forEach(oligo => {
      const oligoId = oligo._id;
      if (!oligoMap[oligoId]) {
        oligoMap[oligoId] = oligo;
      }
    });

    // Now, get the combined oligos
    const combinedOligos = Object.values(oligoMap);

    // Map oligos for the checkbox component
    oligos.value = combinedOligos.map((oligo) => ({
      value: oligo._id,
      name: oligo.name + (oligo.archived ? ' (Archived)' : ''),
      archived: oligo.archived,
    }));

    // Set the selected oligos
    selectedOligos.value = activeVersionOligoIds;

  } catch (error) {
    console.error('Failed to fetch data:', error);
    router.push('/reagents'); // Redirect if there's an error
  }
}


// Handle form submission
async function handleSubmit() {
  if (confirmationText.value !== 'YES') {
    console.error("Please type 'YES' to confirm before submitting.");
    return;
  }

  try {
    const productData = {
      name: productName.value,
      oligos: selectedOligos.value,
    };
    const response = await productsApi.updateProduct(productId, productData);
    console.log('Product updated successfully:', response);
    router.push('/reagents'); // Redirect to the products list
  } catch (error) {
    console.error('Failed to update product:', error);
  }
}

// Handle cancel button
function handleCancel() {
  router.push('/reagents'); // Redirect to the products list
}
</script>


<template>
  <div class="edit-product-wrapper">
    <form @submit.prevent="handleSubmit">
      <h1 class="form-header">Edit Product</h1>
      <!-- Text Input for Product Name -->
      <FormTextInputItem 
        v-model="productName" 
        section-header="Product Name" 
        placeholder="Enter Product Name" 
      />

      <!-- Checkbox Items for Available Oligos -->
      <FormCheckboxItem
        sectionHeader="Available Oligos"
        :optionsList="oligos"
        v-model:selectionVar="selectedOligos"
      />

      <FormTextInputItem v-model="confirmationText" section-header="Type 'YES' to confirm the above information is correct" />


      <!-- Action Buttons -->
      <div class="action-buttons">
        <FormActionButton
          v-model="confirmationText" 
          buttonText="Submit"
          buttonClass="submit"
        />
        <FormActionButton
          buttonText="Cancel"
          buttonClass="cancel"
          @cancelButtonClicked="handleCancel"
        />
      </div>
    </form>
  </div>
</template>

<style scoped>
.edit-product-wrapper {
  padding: 2rem;
  background-color: #f8f9fa;
  border-radius: 10px;
  max-width: 600px;
  margin: 0 auto;
}

.action-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.form-header {
  color: var(--fwdx-blue);
  font-weight: 700;
  font-size: 26px;
  margin-bottom: 20px;
}
</style>
