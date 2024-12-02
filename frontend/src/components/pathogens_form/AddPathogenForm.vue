<script setup>
import {ref} from 'vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';
import {useRouter} from 'vue-router';
import pathogensApi from '@/services/pathogensApiHelper';

const taxonomicID = ref('')
const commonName = ref('');
const sequence = ref('');

const router = useRouter();
const props = defineProps(['formTitle', 'isEditReport']);

function onCancel() {
  router.push("/pathogens");
}

function onSubmit() {
  console.log(taxonomicID.value)
  console.log(commonName.value)
  console.log(sequence.value)
}
</script>

<template>
  <div class="add-pathogen-form-container">
    <h1 class="form-header">{{ formTitle }}</h1>

    <!-- pathogen ID -->
    <div>
      <FormTextInputItem
          placeholder="Enter here or Upload from text file"
          section-header="Taxonomic ID"
          v-model="taxonomicID"
      />
    </div>

    <!-- pathogen Name -->
    <div>
      <FormTextInputItem
          placeholder="Enter pathogen Name"
          section-header="Common Name"
          v-model="commonName"
      />
    </div>

    <div>
      <FormTextInputItem
          placeholder="Enter pathogen Name"
          section-header="Genomic Sequence"
          v-model="sequence"
      />
    </div>

    <div class="button-group">
      <button class="cancel-button" @click="onCancel">Cancel</button>
      <button class="submit-button" @click="onSubmit">Submit</button>
    </div>

  </div>
</template>

<style scoped>
.add-pathogen-form-container {
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

.pathogen-name {
  display: flex;
  align-items: center;
}

/* General Button Styles */
button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

/* Cancel Button */
button.cancel-button {
  background-color: #f5f5f5;
  color: #333;
  border: 1px solid #ccc;
}

button.cancel-button:hover {
  background-color: #e0e0e0;
  transform: scale(1.05);
}

/* Submit Button */
button.submit-button {
  background-color: #007bff;
  color: #fff;
  border: 1px solid #007bff;
}

button.submit-button:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

/* Disabled Button */
button:disabled {
  background-color: #ccc;
  color: #666;
  cursor: not-allowed;
}

/* Flexbox Alignment for Buttons */
.button-group {
  display: flex;
  gap: 10px;
  justify-content: flex-end; /* Align buttons to the right */
  margin-top: 10px;
}
</style>
