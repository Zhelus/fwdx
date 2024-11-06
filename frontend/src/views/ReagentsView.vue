<!-- 
Page view for main pathogens page
Last edited by: Michael Nguyen
Date: 11/05/24
-->

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

function actionClicked(path, productName) {
  if (path && productName) {
    router.push({ path, query: { productName } });
  }
}

// Sample data for the table
const reagents = [
  { id: 1, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #001", productDescription: "Product Description", numberOfOligos: 3 },
  { id: 2, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #002", productDescription: "Product Description", numberOfOligos: 6 },
  { id: 3, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #003", productDescription: "Product Description", numberOfOligos: 7 },
  { id: 4, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #004", productDescription: "Product Description", numberOfOligos: 5 },
  { id: 5, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #005", productDescription: "Product Description", numberOfOligos: 3 },
  { id: 6, taxonomicName: "Disease Taxonomic Name", productName: "FWDX #006", productDescription: "Product Description", numberOfOligos: 4 },
];
</script>

<template>
  <div class="reagents-wrapper">
    <div class="header-container">
      <h2 class="page-title">Reagents</h2>
    </div>
    <table class="reagents-table">
      <thead>
        <tr>
          <th>Taxonomic Name</th>
          <th>Product Name</th>
          <th>Product Description</th>
          <th>Number of Oligos</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="reagent in reagents" :key="reagent.id">
          <td>{{ reagent.taxonomicName }}</td>
          <td>{{ reagent.productName }}</td>
          <td>{{ reagent.productDescription }}</td>
          <td>{{ reagent.numberOfOligos }}</td>
          <td class="action-buttons">
            <button class="add-button" @click="actionClicked('/reagents/add', reagent.productName)">Add</button>
            <button class="edit-button" @click="actionClicked('/reagents/edit',reagent.productName)">Edit</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.reagents-wrapper {
  padding: 2rem;
  background-color: #f8f9fa; /* Light gray background to make the table stand out */
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
  color: var(--fwdx-blue); /* Project blue color */
}

.add-product-button {
  background-color: #FFC107;
  color: #000;
  border: none;
  border-radius: 5px;
  padding: 6px 12px; /* Matching the size of buttons in the table */
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-product-button:hover {
  background-color: #e0a800;
}

.reagents-table {
  width: 100%;
  border-collapse: collapse;
  background-color: var(--fwdx-white);
  border-radius: 10px;
  border-color: var(--fwdx-blue);
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.reagents-table th {
  background-color: #eef2f7; /* Light background for table header */
  color: var(--fwdx-blue); /* Project blue color for header text */
  font-weight: bold;
  padding: 12px;
  text-align: left;
  border-bottom: 2px solid var(--fwdx-blue); /* Subtle border for separation */
}

.reagents-table td {
  padding: 30px;
  color: #000; /* Black color for table content */
  border-bottom: 1px solid var(--fwdx-blue); /* Border for row separation */
}

.reagents-table tr:hover {
  background-color: #f1f5fa; /* Hover effect for better interactivity */
}

button { 
    flex: 1;
    padding: 10px 0;
    font-size: 14px;
}

.action-buttons {
  display: flex;
  gap: 10px;
}

.add-button, .edit-button {
  padding: 6px 12px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-button {
  background-color: #FFC107;
  color: #000;
}

.add-button:hover {
  background-color: #e0a800;
}

.edit-button {
  background-color: #1A1A3A;
  color: #FFF;
}

.edit-button:hover {
  background-color: #14122b;
}
</style>
