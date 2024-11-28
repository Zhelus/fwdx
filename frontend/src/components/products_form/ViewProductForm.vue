<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import productsApi from '@/services/productsApiHelper';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';
import FormActionButton from '@/components/report_form/FormActionButton.vue';

const route = useRoute();
const router = useRouter();
const productId = route.params.productId || route.query.id;

// State variables
const productName = ref('');
const versions = ref([]);
const activeVersionIndex = ref(0);
const totalVersions = ref(0);
const oligos = ref([]);

// Fetch product data on mount
async function fetchProduct() {
  try {
    const productData = await productsApi.getProductById(productId);
    productName.value = productData.name;
    versions.value = productData.versions;
    activeVersionIndex.value = productData.active_version_index;
    totalVersions.value = versions.value.length;

    // Get oligos from the active version
    oligos.value = versions.value[activeVersionIndex.value];
  } catch (error) {
    console.error('Failed to fetch product:', error);
  }
}

// Handle Return button
function handleReturn() {
  router.push('/reagents'); // Redirect to the products list
}

onMounted(() => {
  fetchProduct();
});
</script>

<template>
  <div class="view-product-wrapper">
    <h1 class="form-header">View Product</h1>

    <!-- Product Name -->
    <FormTextInputItem
      v-model="productName"
      section-header="Product Name"
      placeholder="Product Name"
      readonly
    />

    <!-- Version Info -->
    <FormTextInputItem
      :model-value="`${activeVersionIndex + 1} / ${totalVersions}`"
      section-header="Active Version"
      readonly
    />

    <!-- Oligo Details -->
    <div v-for="(oligo, index) in oligos" :key="index" class="oligo-item">
      <FormTextInputItem
        :model-value="oligo.sequence"
        :section-header="oligo.name"
        placeholder="Oligo Sequence"
        readonly
      />
    </div>

    <!-- Return Button -->
    <div class="action-buttons">
      <FormActionButton
        buttonText="Return"
        buttonClass="cancel"
        @cancelButtonClicked="handleReturn"
      />
    </div>
  </div>
</template>

<style scoped>
.view-product-wrapper {
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
    border-radius: 10px;
    padding: 30px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    max-width: 800px;
    margin: 0 auto;
}

.form-header {
  color: var(--fwdx-blue);
  font-weight: 700;
  font-size: 26px;
  margin-bottom: 20px;
}

.oligo-item {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

button {
    padding: 12px 20px;
    font-size: 16px;
}
</style>
