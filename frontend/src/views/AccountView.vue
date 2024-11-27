<template>
  <div class="accounts-wrapper">
    <div class="header-container">
      <h2 class="page-title">Accounts</h2>
      <button class="add-product-button" @click="navigateTo('/accounts/add', '')">Add Account</button>
    </div>
    <table class="accounts-table">
      <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Phone Number</th>
        <th>Email</th>
        <th>Access Level</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="account in filteredAccounts" :key="account.id">
        <td>{{ account.first_name }}</td>
        <td>{{ account.last_name }}</td>
        <td>{{ account.phone_number }}</td>
        <td>{{ account.email }}</td>
        <td>{{ account.access_level }}</td>
        <td class="action-buttons">
          <button class="edit-button" @click="editAccount(account)">Edit</button>
          <button class="delete-button" @click="promptDelete(account)">Delete</button>
        </td>
      </tr>
      </tbody>
    </table>
    <div class="modal-mask" v-if="showModal">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <h3>Delete Account</h3>
          </div>
          <div class="modal-body">
            <p>Do you want to delete "{{ currentAccount.first_name }} {{ currentAccount.last_name }}" ({{ currentAccount.email }}) from account list?</p>
          </div>
          <div class="modal-footer">
            <button @click="showModal = false" class="modal-default-button">Cancel</button>
            <button @click="deleteAccount(currentAccount.id)" class="modal-delete-button">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import usersApiHelper from "@/services/usersApiHelper.js";
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const showModal = ref(false);
const currentAccount = ref({});
const accounts = ref([]);
const filters = ref({
  global: { value: null, matchMode: "contains" },
  first_name: { value: null, matchMode: "startsWith" },
  last_name: { value: null, matchMode: "startsWith" },
  phone_number: { value: null, matchMode: "contains" },
  email: { value: null, matchMode: "contains" },
  access_level: { value: null, matchMode: "equals" }
});


const filteredAccounts = computed(() => {
  return accounts.value.filter(account => {
    // Here you can implement more complex filtering based on above filter settings
    return Object.keys(filters.value).every(key => {
      const filter = filters.value[key];
      if (!filter.value) return true;
      const accountValue = account[key] && account[key].toString().toLowerCase();
      const filterValue = filter.value.toLowerCase();
      switch (filter.matchMode) {
        case "contains": return accountValue.includes(filterValue);
        case "startsWith": return accountValue.startsWith(filterValue);
        case "equals": return accountValue === filterValue;
        default: return true;
      }
    });
  });
});


onMounted(async () => {
  await fetchUsers();
})

async function fetchUsers() {
    usersApiHelper.getAllUsers()
        .then(response => {
          //console.log("API Response: ", response);
          if (response.status === 'success'  && Array.isArray(response.data)) {
            console.log(response.data)
            accounts.value = response.data.map(user => ({
              ...user,
              id: user._id,
              first_name: user.first_name,
              last_name: user.last_name,
              phone_number: user.phone_number,
              email: user.email,
              access_level: user.access_level,
            }));
            //console.log("Successfully loaded user accounts.")
          } else {
            alert(response.data.message)
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
        });
}


function navigateTo(path, userId) {
  router.push({ path, query: { userId } });
}

function promptDelete(account) {
  currentAccount.value = account;
  showModal.value = true;
}

function editAccount(account){
  router.push({ name: 'editAccount', params: {userId: account.id}});
}

async function deleteAccount(userId) {
  console.log("Deleting account with ID:", userId);
  showModal.value = false; // Hide modal independently of the result

  usersApiHelper.deleteUser(userId)
      .then(response => {
        console.log("Delete response:", response);
        if (response.status === 'success') {
          // Find index of the user in the local list and remove it
          const index = accounts.value.findIndex(acc => acc.id === userId);
          if (index !== -1) {
            accounts.value.splice(index, 1);
          }
        } else {
          alert('Failed to delete the account: ' + response.message);
        }
      })
      .catch(error => {
        console.error('Error deleting account:', error);
      });
}
</script>

<style scoped>
.accounts-wrapper {
  padding: 2rem;
  background-color: #f8f9fa; /* Consistent background color */
  border-radius: 10px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1); /* Consistent shadow for depth */
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
  color: var(--fwdx-blue); /* Ensuring consistent use of brand color */
}

.add-product-button {
  background-color: #FFC107; /* Consistent button color */
  color: #000;
  border: none;
  border-radius: 5px;
  padding: 6px 12px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.add-product-button:hover {
  background-color: #e0a800;
}

.accounts-table {
  width: 100%;
  border-collapse: collapse;
  background-color: var(--fwdx-white); /* Using consistent table background */
  border-radius: 10px;
  border-color: var(--fwdx-blue); /* Consistent border color */
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Consistent shadow */
}

.accounts-table th {
  background-color: #eef2f7; /* Light background for headers */
  color: var(--fwdx-blue);
  font-weight: bold;
  padding: 12px;
  text-align: left;
  border-bottom: 2px solid var(--fwdx-blue); /* Consistent header border */
}

.accounts-table td {
  padding: 30px;
  color: #000; /* Text color for better readability */
  border-bottom: 1px solid var(--fwdx-blue); /* Consistent row separation */
}

.action-buttons {
  display: flex;
  gap: 10px;
}

.edit-button, .delete-button {
  padding: 6px 12px;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

.edit-button {
  background-color: #1A1A3A;
  color: #FFF;
}

.edit-button:hover {
  background-color: #14122b;
}

.delete-button {
  background-color: #d9534f;
  color: #fff;
}

.delete-button:hover {
  background-color: #c9302c;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Darker mask for better focus */
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-wrapper {
  padding: 20px;
}

.modal-container {
  background: #fff;
  border-radius: 5px;
  padding: 20px;
  min-width: 300px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Adding depth */
}

.modal-header h3 {
  margin-top: 0;
  color: #333; /* Consistent dark text */
}

.modal-body p {
  margin: 0;
  color: #333; /* Consistent text color */
}

.modal-footer {
  display: flex;
  justify-content: space-between; /* Even spacing */
  padding: 20px;
}

.modal-default-button, .modal-delete-button {
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  border: none;
  font-weight: bold;
  color: #fff;
  flex-grow: 1;
  margin: 0 10px;
}

.modal-default-button {
  background-color: #ccc;
  color: #333;
}

.modal-delete-button {
  background-color: #d9534f;
  color: white;
}

.modal-default-button:hover {
  background-color: #bbb;
}

.modal-delete-button:hover {
  background-color: #c9302c;
}
</style>


