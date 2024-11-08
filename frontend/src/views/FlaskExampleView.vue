<!--
Example file for how to connect Flask API calls to Vue frontend

Last edited by: Harrison Leath
Date: 10/30/24
-->

<script setup>
import {ref} from 'vue';
import api from "@/services/apiClient.js";

const result = ref("")
const search = ref("")

function flask_integration_test() {
  api.getDebug()
      .then(response => {
        console.log("API call was successful.");
        result.value = response.data; // Assign the data to the reactive variable
      })
      .catch(error => {
        console.error("API call failed:", error);
        result.value = "Error occurred while fetching data.";
      });
}

function search_mongo_integration_test() {
  api.getPathogen()
      .then(response => {
        console.log("API call was successful.");
        search.value = response.data; // Assign the data to the reactive variable
      })
      .catch(error => {
        console.error("API call failed:", error);
        search.value = "Error occurred while fetching data.";
      });
}
</script>

<template>
  <div style="display: flex; flex-direction: column;">
    <h1>Flask Example View</h1>
    <h3>This is an example implementation of how to connect Vue components and the Flask backend.</h3>
    <p>To get started, make sure both the frontend and backend are running locally on your machine. You can check the
      log output in Flask to ensure a 200 was returned.</p>
    <button @click="flask_integration_test()">Send GET request to /api/debug</button>
    <h3>Result of the API call:</h3>
    <p>{{ result }}</p>

    <button @click="search_mongo_integration_test()">Send GET request to /api/debug</button>
    <h3>Result of the API call:</h3>
    <p>{{ search }}</p>
  </div>
</template>

<style scoped>
h1, h3, p {
  color: var(--fwdx-blue);
  margin: 5px;
}

button {
  width: 250px;
  height: 60px;
  margin: 20px 5px;
}
</style>