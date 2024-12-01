import api from "@/services/apiClient.js";

/*
const pathogensApi = {
   *
   *  Fetch all pathogens.
   * @returns {Promise<Array>} A list of pathogens.
   *
  async getPathogens() {
    try {
      const response = await axios.get(`${BASE_URL}`);
      return response.data; // Assuming the API returns an array of pathogens
    } catch (error) {
      console.error('Error fetching pathogens:', error);
      throw error;
    }
  },


   *
   * Add a new pathogen.
   * @param {Object} pathogenData - The data for the new pathogen.
   * @returns {Promise<Object>} The created pathogen object.
   *
  async addPathogen(pathogenData) {
    try {
      const response = await axios.post(BASE_URL, pathogenData);
      return response.data; // Assuming the API returns the created pathogen
    } catch (error) {
      console.error('Error adding new pathogen:', error);
      throw error;
    }
  },
};
*/

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

//Call specifically from PathogenDetailedView.vue to produce the table
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



    createPathogen(pathogenID) {
        return new Promise((resolve, reject) => {
            api.createPathogen(pathogenID)
                .then(response => {
                    console.log("API call successful: Created pathogen.");
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error creating new pathogen."));
                });
        });
    },

};