import api from "@/services/apiClient.js"

export default {
    getUser(user_id) {
        return new Promise(function (resolve, reject) {
            api.getUser(user_id)
                .then(response => {
                    console.log("API call was successful");
                    resolve({
                        status: 'success',
                        message: response.data.message || 'Fetch successful',
                        data: response.data['user']
                    });
                })
                .catch(error => {
                    console.error("API called failed:", error);
                    reject(Error('Error fetching user with id: ${user_id}'));
                });
        });
    },
    getAllUsers(){
        return new Promise(function(resolve, reject) {
            api.getAllUsers()
                .then(response => {
                    console.log("API Successful -- get all users.");
                    resolve({
                        status: 'success',
                        message: response.data.message || 'Fetch successful',
                        data: response.data['users']
                    });
                })
                .catch(error => {
                    console.error("API called failed", error);
                    reject(Error("Error fetching all user data."));
                });
        });
    },
    updateUser(user_id, updatedUserData) {
        return new Promise(function(resolve, reject){
            api.updateUser(user_id,updatedUserData)
                .then(response => {
                    console.log("API call was successful");
                    resolve({
                        status: 'success',  // Standardize success status
                        message: response.data.message || 'Update successful',
                        data: response.data // Include all data from the response
                    });
                })
                .catch(error => {
                    console.error("API called failed", error);
                    reject(Error("Error updating user data."));
                });
        });
    },
    deleteUser(user_id) {
        return new Promise(function(resolve,reject){
            api.deleteUser(user_id)
                .then(response => {
                    console.log("API call was successful");
                    resolve({
                        status: 'success',  // Standardize success status
                        message: response.data.message || 'Deletion successful',
                        data: response.data // Include all data from the response
                    });
                })
                .catch(error => {
                    console.error("API called failed:", error);
                    reject(Error("Error occured while fetching data"));
                });
        });
    },
    loginUser(credentials) {
        return new Promise(function(resolve,reject){
            api.loginUser(credentials)
                .then(response => {
                    console.log("API call was successful");
                    resolve({
                        status: 'success',  // Standardize success status
                        message: response.data.message || 'Login successful',
                        data: response.data // Include all data from the response
                    });
                })
                .catch(error => {
                    console.error("API called failed:", error);
                    reject(Error("Error occurred while logging in"));
                });
        });
    },
    logoutUser(user_id) {
        return new Promise(function(resolve,reject){
            api.logoutUser(user_id)
                .then(response => {
                    console.log("API call was successful");
                    resolve({
                        status: 'success',  // Standardize success status
                        message: response.data.message || 'Logout successful',
                        data: response.data // Include all data from the response
                    });
                })
                .catch(error => {
                    console.error("API called failed:", error);
                    reject(Error("Error logging out user"));
                });
        });
    },
    registerUser() {
        return new Promise(function(resolve,reject){
            api.registerUser()
                .then(response => {
                    console.log("API call was successful");
                    resolve({
                        status: 'success',  // Standardize success status
                        message: response.data.message || 'Registration successful',
                        data: response.data // Include all data from the response
                    });
                })
                .catch(error => {
                    console.error("API called failed:", error);
                    reject(Error("Error registering user"));
                });
        });
    }
}