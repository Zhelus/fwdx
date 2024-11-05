<!-- 
Page view for adding a new reagent 
Last edited by: Michael Nguyen
Date: 11/05/24
-->

<script setup>
import { ref } from 'vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';
import FormCheckboxItem from '@/components/report_form/FormCheckboxItem.vue';
import FormActionButton from '@/components/report_form/FormActionButton.vue';
import { useRouter } from 'vue-router'

const reagentName = ref('');
const isReagentActive = ref(false);
const reagentDescription = ref('');
const reagentString = ref('');
const isReagentNegative = ref(false);
const confirmationText = ref('');
const props = defineProps(['formTitle', 'showFrequency', 'isEditReport'])
const router = useRouter();


function cancelClicked() {
  console.log("Clicked cancel button");
  router.push("/reagents");}

function addReagentClicked() {
  // Logic to handle adding the reagent, such as submitting the form
}
</script>

<template>
  <div class="add-reagent-form-container">
    <h1 class="form-header">{{ formTitle }}</h1>
    <!-- Reagent Name and Active Checkbox -->
    <div class="reagent-name-active">
      <FormTextInputItem 
        v-model="reagentName" 
        section-header="Oligo Name" 
        placeholder="Enter Oligo Name" 
      />
      <FormCheckboxItem 
        :options-list="[{ name: 'Oligo Active?', value: 'active' }]" 
        v-model="isReagentActive" 
      />
    </div>

    <!-- Reagent Description -->
    <FormTextInputItem 
      v-model="reagentDescription" 
      section-header="Oligo Description" 
      placeholder="Enter Description" 
    />

    <!-- Reagent String and Upload File Button -->
    <div class="reagent-string-upload">
      <FormTextInputItem 
        v-model="reagentString" 
        section-header="Oligo Strings" 
        placeholder="Enter here or Upload from text file" 
      />
      <FormActionButton 
        button-text="Upload File" 
        button-class="upload-file-button" 
      />
    </div>

    <!-- Reagent Negative Checkbox -->
    <FormCheckboxItem 
      :options-list="[{ name: 'Oligo Negative?', value: 'negative' }]" 
      v-model="isReagentNegative" 
    />

    <!-- Confirmation Text Input -->
    <FormTextInputItem 
      v-model="confirmationText" 
      section-header="Type 'YES' to confirm the above information is correct" 
      placeholder="Type 'YES' here" 
    />

    <!-- Action Buttons -->
    <div class="form-button-container">
      <FormActionButton 
        button-text="Cancel" 
        button-class="cancel" 
        @click="cancelClicked" 
      />
      <FormActionButton 
        button-text="Add Reagent" 
        button-class="submit" 
        @click="addReagentClicked" 
      />
    </div>
  </div>
</template>

<style scoped>
.add-reagent-form-container {
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

.reagent-name-active {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.reagent-string-upload {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.form-button-container {
  display: flex;
  gap: 20px;
  margin-top: 20px;
}

button {
  padding: 12px 20px;
  font-size: 16px;
}
</style>
