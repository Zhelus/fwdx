<script setup>
import { ref, onMounted } from 'vue';
import oligosApi from '@/services/oligosApiHelper';
import productsApi from '@/services/productsApiHelper';
import { useRouter } from 'vue-router';
import FormActionButton from '@/components/report_form/FormActionButton.vue';
import FormCheckboxItem from './ProductFormCheckBoxItem.vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';

const router = useRouter();

// Bindings for the form
const productName = ref('');
const oligos = ref([]);
const selectedOligos = ref([]);
const confirmationText = ref('');
const props = defineProps(['formTitle', 'isEditReport']);

// Fetch active oligos on mount
async function fetchActiveOligos() {
  try {
    const fetchedOligos = await oligosApi.getActiveOligos();
    // Map oligos for use in the checkbox component
    oligos.value = fetchedOligos.map((oligo) => ({
      value: oligo._id,
      name: oligo.name,
    }));
  } catch (error) {
    console.error('Failed to fetch active oligos:', error);
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
    const response = await productsApi.saveNewProduct(productData);
    console.log('Product created successfully:', response);
    router.push('/products'); // Redirect to the products list
  } catch (error) {
    console.error('Failed to create product:', error);
  }
}

// Handle cancel button
function handleCancel() {
  router.push('/reagents'); // Redirect to the products list
}

// Fetch oligos when the component is mounted
onMounted(() => {
  fetchActiveOligos();
});
</script>

<template>
  <div class="add-product-wrapper">
    <form @submit.prevent="handleSubmit">
      <h1 class="form-header">{{ formTitle }}</h1>
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
.add-product-wrapper {
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
