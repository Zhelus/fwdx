<!-- 
Form to view individual oligo details
Last edited by: Michael Nguyen
Date: 11/21/24
-->

<script setup>
import { ref, onMounted } from 'vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';
import OligoCheckboxForm from '@/components/oligos_form/OligoFormCheckBoxItem.vue';
import FormActionButton from '@/components/report_form/FormActionButton.vue';
import { useRoute, useRouter } from 'vue-router';
import oligosApi from '@/services/oligosApiHelper';

const oligoName = ref('');
const oligoString = ref('');
const dnaStrandPositive = ref(false); // Default to false
const router = useRouter();
const route = useRoute(); // Access the route parameters

// Fetch the oligo details on mount
async function fetchOligoDetails() {
  const oligoId = route.query.id; // Get the ID from query parameters
  if (!oligoId) {
    console.error("No oligo ID provided.");
    router.push('/oligos');
    return;
  }

  try {
    const oligo = await oligosApi.getOligoById(oligoId);
    // Populate the fields
    oligoName.value = oligo.name;
    oligoString.value = oligo.sequence;
    dnaStrandPositive.value = oligo.dna_strand_positive;
  } catch (error) {
    console.error("Failed to fetch oligo details:", error);
    router.push('/oligos');
  }
}

function doneClicked() {
  router.push('/oligos'); // Redirect back to Oligos Home Page
}

onMounted(() => {
  fetchOligoDetails();
});
</script>

<template>
  <div class="view-oligo-form-container">
    <h1 class="form-header">View Oligo</h1>
    <!-- Oligo Name -->
    <div class="oligo-name">
      <FormTextInputItem 
        v-model="oligoName" 
        section-header="Oligo Name" 
        placeholder="N/A" 
        readonly 
      />
    </div>

    <!-- Oligo String -->
    <div class="oligo-string">
      <FormTextInputItem 
        v-model="oligoString" 
        section-header="Oligo String" 
        placeholder="N/A" 
        readonly 
      />
    </div>

    <!-- DNA Strand Positive Checkbox -->
    <OligoCheckboxForm
      section-header="DNA Strand Positive?"
      v-model="dnaStrandPositive"
      :readonly="true" 
    />

    <!-- Done Button -->
    <div class="form-button-container">
      <FormActionButton 
        button-text="Return" 
        button-class="cancel" 
        @cancelButtonClicked="doneClicked" 
      />
    </div>
  </div>
</template>

<style scoped>
.view-oligo-form-container {
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

.oligo-name,
.oligo-string {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

button {
  padding: 12px 20px;
  font-size: 16px;
}
</style>
