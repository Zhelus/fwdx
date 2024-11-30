<!-- 
Form to add oligo
Last edited by: Michael Nguyen
Date: 11/21/24
-->
<script setup>
import { ref } from 'vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';
import FormCheckboxItem from './OligoFormCheckBoxItem.vue'; // Import the custom checkbox component
import FormActionButton from '@/components/report_form/FormActionButton.vue';
import { useRouter } from 'vue-router';
import oligosApi from '@/services/oligosApiHelper';


const oligoName = ref('');
const oligoString = ref('');
const dnaStrandPositive = ref(true); // Bind directly to the checkbox
const confirmationText = ref('');
const props = defineProps(['formTitle', 'isEditReport']);
const router = useRouter();

function cancelClicked() {
  console.log("Clicked cancel button");
  router.push("/oligos");
}

async function submitClicked() {
  if (confirmationText.value !== "YES") {
    console.error("Please type 'YES' to confirm before submitting.");
    return;
  }

  const oligoData = {
    name: oligoName.value,
    sequence: oligoString.value,
    archived: false,
    dna_strand_positive: dnaStrandPositive.value, // Use the directly bound value
  };

  try {
    const response = await oligosApi.createOligo(oligoData);
    console.log("Oligo created successfully:", response);
    router.push("/oligos"); // Redirect to oligos list after successful creation
  } catch (error) {
    console.error("Failed to create oligo:", error);
  }
}

function handleFileUpload(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      oligoString.value = e.target.result; // Set the file content to the input field
    };
    reader.onerror = () => {
      console.error("Failed to read the file.");
    };
    reader.readAsText(file); // Read file content as text
  }
}

function triggerFileInput() {
  document.getElementById('file-upload').click();
}
</script>

<template>
  <div class="add-oligo-form-container">
    <h1 class="form-header">{{ formTitle }}</h1>
    <!-- Oligo Name -->
    <div class="oligo-name">
      <FormTextInputItem 
        v-model="oligoName" 
        section-header="Oligo Name" 
        placeholder="Enter Oligo Name" 
      />
    </div>

    <!-- Oligo String and Upload File Button -->
    <div class="oligo-string-upload">
      <FormTextInputItem 
        v-model="oligoString" 
        section-header="Oligo Strings" 
        placeholder="Enter here or Upload from text file" 
      />
      <!-- Hidden File Input -->
      <input 
        type="file" 
        accept=".txt" 
        class="hidden-file-input" 
        id="file-upload" 
        @change="handleFileUpload" 
      />
      <!-- Styled Button to Trigger File Upload -->
      <FormActionButton 
        button-text="Choose File" 
        button-class="upload-file-button" 
        @click="triggerFileInput" 
      />
    </div>

    <!-- DNA Strand Positive Checkbox -->
    <FormCheckboxItem 
    v-model="dnaStrandPositive"  
    />
    <FormTextInputItem v-model="confirmationText" section-header="Type 'YES' to confirm the above information is correct" />


    <!-- Confirmation Buttons -->
    <div class="action-buttons">
      <FormActionButton 
      v-model="confirmationText" 
      button-text="Submit" 
      button-class="submit" 
      @click="submitClicked" 
    />
      <FormActionButton 
        button-text="Cancel" 
        button-class="cancel" 
        @cancelButtonClicked="cancelClicked" 
      />
    </div>
  </div>
</template>

<style scoped>
.add-oligo-form-container {
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

.oligo-name {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.oligo-string-upload {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.hidden-file-input {
  display: none; /* Hide the native file input */
}
.action-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

button {
  padding: 12px 20px;
  font-size: 16px;
}
</style>
