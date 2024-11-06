<!-- 
Page view for editing a reagent 
Last edited by: Michael Nguyen 
Date: 11/05/24 
-->

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'

const confirmationText = ref('');
const props = defineProps(['formTitle', 'showFrequency', 'isEditReport'])
const router = useRouter();

const oligoOptions = [
  { name: "Oligo Name 1", id: 1 },
  { name: "Oligo Name 2", id: 2 },
  { name: "Oligo Name 3", id: 3 },
  { name: "Oligo Name 4", id: 4 },
  { name: "Oligo Name 5", id: 5 },
];

function cancelEdit() {
  router.push('/reagents');
}

function saveChanges() {
  // Logic to save changes
  console.log("Changes saved!");
}
</script>

<template>
  <div class="edit-reagent-container">
    <!-- Left Panel with Search Bar and List of Oligos -->
    <div class="left-panel">
      <input type="text" placeholder="Search Oligos..." class="search-bar" />
      <div class="oligo-list">
        <div v-for="oligo in oligoOptions" :key="oligo.id" class="oligo-item">
          {{ oligo.name }}
        </div>
      </div>
    </div>

    <!-- Main Content Area -->
    <div class="main-panel">
      <h1 class="form-header">{{formTitle}}</h1>
      
      <div class="form-group">
        <label for="oligo-name">Oligo Name</label>
        <input type="text" id="oligo-name" v-model="selectedOligo" />

        <label class="checkbox-container">
          <input type="checkbox" /> Oligo Active?
        </label>
      </div>

      <div class="form-group">
        <label for="oligo-description">Oligo Description</label>
        <textarea id="oligo-description" v-model="oligoDescription"></textarea>
      </div>

      <div class="form-group">
        <label for="oligo-string">Reagent Strings</label>
        <input type="text" id="oligo-string" v-model="oligoString" />
        <button class="upload-button">Upload File</button>
      </div>

      <div class="form-group">
        <label class="checkbox-container">
          <input type="checkbox" /> Oligo Negative?
        </label>
      </div>

      <div class="form-group">
        <label>Type "YES" to confirm the above information is correct.</label>
        <input type="text" v-model="confirmationText" placeholder="Type 'YES' here" />
      </div>

      <div class="action-buttons">
        <button class="cancel-button" @click="cancelEdit">Cancel</button>
        <button class="save-button" @click="saveChanges">Save Changes</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.edit-reagent-container {
  display: flex;
  padding: 2rem;
  background-color: #f0f4f8;
}

.left-panel {
  width: 25%;
  padding: 1rem;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.search-bar {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.oligo-list {
  margin-top: 1rem;
}

.oligo-item {
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  cursor: pointer;
}

.oligo-item:hover {
  background-color: #f1f5fa;
}

.main-panel {
  flex-grow: 1;
  margin-left: 2rem;
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.form-header {
  font-size: 24px;
  font-weight: bold;
  color: #1a1a3a;
  margin-bottom: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333;
  font-weight: bold;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

textarea {
  resize: vertical;
  min-height: 100px;
}

.checkbox-container {
  display: flex;
  align-items: center;
  margin-top: 0.5rem;
}

.upload-button {
  margin-left: 0.5rem;
  padding: 6px 12px;
  background-color: #1a1a3a;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.upload-button:hover {
  background-color: #14122b;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

.cancel-button,
.save-button {
  padding: 0.5rem 1.5rem;
  font-size: 14px;
  font-weight: bold;
  border-radius: 4px;
  cursor: pointer;
}

.cancel-button {
  background-color: #ccc;
  color: #333;
}

.save-button {
  background-color: #1a1a3a;
  color: #fff;
}

.save-button:hover {
  background-color: #14122b;
}
</style>
