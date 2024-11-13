<template>
  <div class="edit-account-wrapper">
    <div class="header-container">
      <h2 class="page-title">Edit Account</h2>
    </div>
    <form @submit.prevent="updateAccount">
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
        <label for="role">Role:</label>
        <select id="role" v-model="account.role" required>
          <option value="Technician">Technician</option>
          <option value="Scientist">Scientist</option>
        </select>
      </div>
      <div class="form-group">
        <label for="department">Department:</label>
        <select id="department" v-model="account.department" required>
          <option value="Lab">Lab</option>
          <option value="Administration">Administration</option>
          <option value="Quality Control">Quality Control</option>
        </select>
      </div>
      <div class="form-group">
        <label for="accessLevel">Access Level:</label>
        <select id="accessLevel" v-model="account.accessLevel" required>
          <option value="Admin">Admin</option>
          <option value="User">User</option>
        </select>
      </div>
      <div class="action-buttons">
        <button type="button" class="reset-password-button" @click="resetPassword">Reset Password</button>
        <button type="button" class="cancel-button" @click="cancelAction">Cancel</button>
        <button type="submit" class="submit-button">Update</button>
      </div>
    </form>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const route = useRoute();
const accountId = route.params.id; // Get the account ID from the route parameter
const account = ref({});

const API_URL = 'your-api-url'; // Adjust this to your actual API URL

// Fetch account details
async function fetchAccount() {
  try {
    const response = await axios.get(`${API_URL}/accounts/${accountId}`);
    account.value = response.data; // Assume the API returns the full account object
  } catch (error) {
    console.error('Failed to fetch account:', error);
  }
}

// Update account details
async function updateAccount() {
  try {
    await axios.put(`${API_URL}/accounts/${accountId}`, account.value);
    alert('Account updated successfully');
    router.push('/accounts');
  } catch (error) {
    alert('Failed to update account: ' + (error.response ? error.response.data.message : error.message));
  }
}

function resetPassword() {
  // API call to reset the user's password
  axios.post(`${API_URL}/accounts/reset-password/${accountId}`)
      .then(() => {
        alert('Password reset email sent successfully.');
      })
      .catch((error) => {
        alert('Failed to reset password:', error.response ? error.response.data.message : error.message);
      });
}

function cancelAction() {
  router.push('/accounts'); // Navigate back to accounts view
}

onMounted(fetchAccount);
</script>
<style scoped>
.edit-account-wrapper {
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
  color: var(--fwdx-blue); /* Assuming you have a CSS variable for colors */
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
  width: 100%; /* Fields take full width of the form container */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px; /* Consistent font size for easy readability */
  font-family: Arial, sans-serif; /* Consistent font family across all form elements */
}

.action-buttons {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 20px; /* Added spacing between the last field and buttons */
}

.cancel-button, .submit-button, .reset-password-button {
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

.reset-password-button {
  background-color: #007BFF; /* Bootstrap primary blue for indicative action */
  color: white;
}

.reset-password-button:hover {
  background-color: #0056b3;
}
</style>

