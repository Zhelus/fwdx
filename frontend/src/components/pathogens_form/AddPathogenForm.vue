<script setup>
import { ref } from 'vue';
import FormTextInputItem from '@/components/report_form/FormTextInputItem.vue';
import FormCheckboxItem from '@/components/report_form/FormCheckboxItem.vue';
import FormActionButton from '@/components/report_form/FormActionButton.vue';
import { useRouter } from 'vue-router';
import pathogensApi from '@/services/pathogensApiHelper';

const pathogenName = ref('');
const pathogenString = ref('');
const dnaStrandPositive = ref(true); // Bind directly to the checkbox
const confirmationText = ref('');
const props = defineProps(['formTitle', 'isEditReport']);
const router = useRouter();

function cancelClicked() {
  console.log("Clicked cancel button");
  router.push("/pathogens");
}

async function submitClicked() {
  if (confirmationText.value !== "YES") {
    console.error("Please type 'YES' to confirm before submitting.");
    return;
  }

  const pathogenData = {
    name: pathogenName.value,
    sequence: pathogenString.value,
    archived: false,
    dna_strand_positive: dnaStrandPositive.value, // Use the directly bound value
  };

  try {
    const response = await pathogensApi.createpathogen(pathogenData);
    console.log("pathogen created successfully:", response);
    router.push("/pathogens"); // Redirect to pathogens list after successful creation
  } catch (error) {
    console.error("Failed to create pathogen:", error);
  }
}

function handleFileUpload(event) {
  const file = event.target.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      pathogenString.value = e.target.result; // Set the file content to the input field
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
  <div class="add-pathogen-form-container">
    <h1 class="form-header">{{ formTitle }}</h1>
    
    <!-- pathogen ID -->
    <div class="pathogen-id-upload">
      <FormTextInputItem 
        v-model="PathogensDetailedView" 
        section-header="Unique Pathogen Identifier" 
        placeholder="Enter here or Upload from text file" 
      /> 
    </div>

    <!-- pathogen Name -->
    <div class="pathogen-name">
      <FormTextInputItem 
        v-model="pathogenName" 
        section-header="Common Name" 
        placeholder="Enter pathogen Name" 
      />
    </div>

    <div class="pathogen-gene-upload">
    <span class="upload-text">Genomic Sequence File:</span> <!-- Add this text to the left of the button -->

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
        section-header="Upload Genomic Sequence" 
        button-text="Select" 
        button-class="upload-file-button" 
        @click="triggerFileInput" 
    />
    </div>



    <div class="button-group">
    <button class="cancel-button" @click="onCancel">Cancel</button>
    <button class="submit-button" :disabled="isSubmitting" @click="onSubmit">Submit</button>
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
  margin-bottom: 20px;
}

.pathogen-string-upload {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-bottom: 20px;
}

.hidden-file-input {
  display: none; /* Hide the native file input */
}
.pathogen-gene-upload {
  display: flex;
  align-items: center;
  gap: 10px; /* Adjust spacing between the text and the button */
}

.upload-text {
  font-size: 20px; /* Match the button font size */
  font-weight: 700; /* Optional: Make the text bold */
  color: #333; /* Adjust color as needed */
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
