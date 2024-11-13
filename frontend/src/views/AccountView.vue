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
        <th>Role</th>
        <th>Department</th>
        <th>Access Level</th>
        <th>Actions</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="account in accounts" :key="account.id">
        <td>{{ account.firstName }}</td>
        <td>{{ account.lastName }}</td>
        <td>{{ account.phoneNumber }}</td>
        <td>{{ account.email }}</td>
        <td>{{ account.role }}</td>
        <td>{{ account.department }}</td>
        <td>{{ account.accessLevel }}</td>
        <td class="action-buttons">
          <button class="edit-button" @click="navigateTo('/accounts/edit', account.email)">Edit</button>
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
            <p>Do you want to delete "{{ currentAccount.firstName }} {{ currentAccount.lastName }}" ({{ currentAccount.email }}) from account list?</p>
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const showModal = ref(false);
const currentAccount = ref({});
const accounts = ref([
  { id: 1, firstName: "Alice", lastName: "Smith", phoneNumber: "123-456-7890", email: "alice@example.com", role: "Manager", department: "Marketing", accessLevel: "High" },
  { id: 2, firstName: "Bob", lastName: "Johnson", phoneNumber: "123-456-7891", email: "bob@example.com", role: "Staff", department: "Sales", accessLevel: "Medium" },
  { id: 3, firstName: "Carol", lastName: "Williams", phoneNumber: "123-456-7892", email: "carol@example.com", role: "Admin", department: "IT", accessLevel: "Admin" },
]);

function navigateTo(path, username) {
  router.push({ path, query: { username } });
}

function promptDelete(account) {
  currentAccount.value = account;
  showModal.value = true;
}

function deleteAccount(id) {
  // Implement deletion logic here
  console.log("Deleting account with ID:", id);
  showModal.value = false;
  // Update accounts list after deletion
  const index = accounts.value.findIndex(acc => acc.id === id);
  if (index !== -1) {
    accounts.value.splice(index, 1);
  }
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


