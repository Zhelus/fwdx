<!--
Page view for main account page view
Last edited by: Nicholas Tullbane
Date: 11/12/24
-->

<template>
  <div class="accounts-wrapper">
    <div class="header-container">
      <h2 class="page-title">Add New Account</h2>
    </div>
    <form @submit.prevent="addAccount">
      <div class="form-group">
        <label for="firstName">First Name:</label>
        <input type="text" id="firstName" v-model="account.firstName" required>
      </div>
      <div class="form-group">
        <label for="lastName">Last Name:</label>
        <input type="text" id="lastName" v-model="account.lastName" required>
      </div>
      <div class="form-group">
        <label for="phoneNumber">Phone Number:</label>
        <input type="tel" id="phoneNumber" v-model="account.phoneNumber" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="account.email" required>
      </div>
      <div class="form-group">
        <label for="accessLevel">Access Level:</label>
        <select id="accessLevel" v-model="account.accessLevel" required>
          <option value="Admin">Admin</option>
          <option value="User">User</option>
        </select>
      </div>
      <div class="action-buttons">
        <button type="button" class="cancel-button" @click="cancelAction">Cancel</button>
        <button type="submit" class="submit-button">Submit</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const account = ref({
  firstName: '',
  lastName: '',
  phoneNumber: '',
  email: '',
  role: '',
  department: '',
  accessLevel: ''
});

const API_URL = 'your-api-url'; // Adjust this to your actual API URL

async function addAccount() {
  try {
    const response = await axios.post(`${API_URL}/accounts/create`, account.value);
    alert('Account added successfully: ' + response.data);
    account.value = {}; // Reset form fields after successful submission
    router.push('/accounts');
  } catch (error) {
    alert('Failed to add account: ' + (error.response ? error.response.data.message : error.message));
  }
}

function cancelAction() {
  router.push('/accounts'); // Navigate back or to a specific route on cancel
}
</script>

<style scoped>
.accounts-wrapper {
  padding: 2rem;
  background-color: #f8f9fa; /* Light gray background to make the form stand out */
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  width: 50%; /* Set the width to half of the page */
  margin: 0 auto; /* Center the form horizontally */
  max-width: 600px; /* Optional: you can set a max-width to prevent it from being too wide on larger screens */
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
  color: var(--fwdx-blue); /* Specific blue color from your project */
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #333; /* Darker text for better visibility */
  font-size: 16px; /* Consistent font size for labels */
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="tel"],
.form-group select {
  width: 100%; /* Uniform width */
  padding: 10px; /* Consistent padding */
  border: 1px solid #ccc; /* Consistent border */
  border-radius: 5px; /* Rounded corners for aesthetics */
  font-size: 16px; /* Consistent font size for easy readability */
  font-family: Arial, sans-serif; /* Consistent font family across all form elements */
}

.action-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 20px; /* Added spacing between the last field and buttons */
}

.cancel-button, .submit-button {
  background-color: #FFC107;
  color: #000;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
  font-size: 16px; /* Matching the font size of input fields */
  font-family: Arial, sans-serif; /* Ensuring consistency in font across all clickable elements */
}

.cancel-button {
  background-color: #ccc; /* Light gray for cancel button */
}

.cancel-button:hover {
  background-color: #bbb;
}

.submit-button:hover {
  background-color: #e0a800;
}
</style>
