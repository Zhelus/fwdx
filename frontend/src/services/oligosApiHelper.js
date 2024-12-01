import api from "@/services/apiClient.js";
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';
const $toast = useToast(); // Initialize toast

export default {
    getAllOligos() {
        return new Promise((resolve, reject) => {
            api.getAllOligos()
                .then(response => {
                    console.log("API call successful: Fetch all oligos.");
                    const oligosData = response.data['oligos'];
                    resolve(oligosData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error fetching all oligos."));
                });
        });
    },
    getActiveOligos() {
        return new Promise((resolve, reject) => {
            api.getActiveOligos()
                .then(response => {
                    console.log("API call successful: Fetch active oligos.");
                    const oligosData = response.data['oligos'];
                    resolve(oligosData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error fetching active oligos."));
                });
        });
    },
    getOligoById(oligoId) {
        return new Promise((resolve, reject) => {
            api.getOligoById(oligoId)
                .then(response => {
                    console.log("API call successful: Fetch oligo by ID.");
                    const oligo = response.data['oligo'];
                    resolve(oligo);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error(`Error fetching oligo with ID: ${oligoId}`));
                });
        });
    },
    createOligo(oligoData) {
        return new Promise((resolve, reject) => {
            api.createOligo(oligoData)
                .then(response => {
                    console.log("API call successful: Create oligo.");
                    $toast.success('Oligo created successfully!', {
                        position: 'top-right',
                        duration: 3000,
                      });
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    $toast.error('Failed to create oligo. Please try again.', {
                        position: 'top-right',
                        duration: 3000,
                      });
                    reject(Error("Error creating new oligo."));
                });
        });
    },
    archiveOligo(oligoId) {
        return new Promise((resolve, reject) => {
            api.archiveOligo(oligoId)
                .then(response => {
                    console.log("API call successful: Archive oligo.");
                    $toast.success('Oligo successfully archived!', {
                        position: 'top-right',
                        duration: 3000,
                      });
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    $toast.error('Failed to archive product. Please try again.', {
                        position: 'top-right',
                        duration: 3000,
                      });
                    reject(Error(`Error archiving oligo with ID: ${oligoId}`));
                });
        });
    }
};
