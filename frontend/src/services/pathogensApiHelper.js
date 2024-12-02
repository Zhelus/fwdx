import api from "@/services/apiClient.js";

export default {

    getPathogens() {
        return new Promise((resolve, reject) => {
            api.getPathogens()
                .then(response => {
                    console.log("API call successful: Fetch active pathogens.");
                    const pathogensData = response.data['pathogens'];
                    resolve(pathogensData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error fetching active pathogens."));
                });
        });
    },

    getPathogenById(pathogenId) {
        return new Promise((resolve, reject) => {
            api.getPathogenById(pathogenId)
                .then(response => {
                    console.log("API call successful: Fetch pathogen by ID.");
                    const pathogen = response.data['pathogen'];
                    resolve(pathogen);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error(`Error fetching pathogen with ID: ${pathogenId}`));
                });
        });
    },

    // Call specifically from PathogenDetailedView.vue to produce the table
    async getPathogenByTaxonomicID(taxonomicID) {
        try {
            const response = await api.getPathogenByTaxID(taxonomicID);

            console.log("API Response for taxonomicID:", response.data);
            return response.data.pathogen; // Adjust based on your backend response
        } catch (error) {
            console.error(`Error fetching pathogen by taxonomicID:`, error);
            throw error;
        }
    },


    getAllPathogens() {
        return new Promise((resolve, reject) => {
            api.getAllPathogens()
                .then(response => {
                    console.log("API call successful: Fetch all pathogens.");
                    const pathogenData = response.data;
                    resolve(pathogenData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error fetching all pathogens."));
                });
        });
    },


    createPathogen(pathogen) {
        return new Promise((resolve, reject) => {
            api.createPathogen(JSON.stringify(pathogen))
                .then(response => {
                    console.log("API call successful: Created pathogen.");
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(new Error("Error creating new pathogen."));
                });
        });
    },


};