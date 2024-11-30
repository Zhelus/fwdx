<template>
  <div class="edit-account-wrapper">
    <div class="header-container">
      <h2 class="page-title">Edit Account</h2>
    </div>
    <form @submit.prevent="updateAccount">
      <div class="form-group">
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" v-model="currentAccount.first_name" required>
      </div>
      <div class="form-group">
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" v-model="currentAccount.last_name" required>
      </div>
      <div class="form-group">
        <label for="phone_number">Phone Number:</label>
        <input type="tel" id="phone_number" v-model="currentAccount.phone_number" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="currentAccount.email" required>
      </div>
      <div class="form-group">
        <label for="access_level">Access Level:</label>
        <select id="access_level" v-model="currentAccount.access_level" required>
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
import usersApiHelper from "@/services/usersApiHelper.js";
import { ref, onMounted } from 'vue';
import {useRoute, useRouter} from 'vue-router';

const route = useRoute(); //Gives access to the current route
const router = useRouter();
const currentAccount = ref({});

onMounted(async () => {
  const userId = route.params.userId;
  await fetchUser(userId);
})

// Fetch account details
async function fetchUser(userId) {
  usersApiHelper.getUser(userId)
      .then(user => {
        console.log("API Response: ", user);
        if(user.status === 'success'){
          currentAccount.value = {
            first_name: user.data.first_name,
            last_name: user.data.last_name,
            phone_number: user.data.phone_number,
            email: user.data.email,
            access_level: user.data.access_level
          };
        } else {
          alert(user.data.message)
        }
      })
      .catch(error => {
        if (error.response) {
          // The request was made and the server responded with a status code
          // that falls out of the range of 2xx
          console.error('Error:', error.response.data);
          alert(error.response.data.message || 'User accounts retrieval failed, please try again.');
        } else if (error.request) {
          // The request was made but no response was received
          console.error('Error:', error.request);
          alert('No response from server. Check your network connection.');
        } else {
          // Something happened in setting up the request that triggered an Error
          console.error('Error:', error.message);
          alert('Error, please try again.');
        }
      })
}

// Update account details
function updateAccount(userId) {
  usersApiHelper.updateUser(userId, currentAccount.value)
      .then(response => {
        console.log(typeof userId)
        console.log(response.data)
        if(response.status === 'success'){
          router.push("/accounts");
          console.log("Update is successful in EditAccountView")
        } else {
          alert('Failed to update the account: ' + response.message);
        }
      })
      .catch(error => {
        console.error('Error updating account:', error)
        alert('Error during updating account: ' + error.message);
      });
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

