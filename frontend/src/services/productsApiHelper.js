import api from "@/services/apiClient.js";

export default {
    getProductById(productId) {
        return new Promise(function (resolve, reject) {
            api.getProductById(productId)
                .then(response => {
                    console.log("API call was successful: Fetch product by ID.");
                    console.log(response.data);
                    const productData = response.data['product'];
                    resolve(productData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error(`Error fetching product with ID: ${productId}`));
                });
        });
    },
    getAllProducts() {
        return new Promise(function (resolve, reject) {
            api.getAllProducts()
                .then(response => {
                    console.log("Successful API call: Fetch all products.");
                    const productsData = response.data['products'];
                    resolve(productsData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error fetching all products."));
                });
        });
    },
    getAllProductsWithOligoNames() {
        return new Promise(function (resolve, reject) {
            api.getAllProductsByOligoNames()
                .then(response => {
                    console.log("Successful API call: Fetch all products with oligo names.");
                    const productsData = response.data['products'];
                    resolve(productsData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error fetching all products with oligo names."));
                });
        });
    },
    saveNewProduct(productData) {
        return new Promise(function (resolve, reject) {
            api.createProduct(productData)
                .then(response => {
                    console.log("API call was successful: Save new product.");
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error creating new product."));
                });
        });
    },
    deleteProduct(productId) {
        return new Promise(function (resolve, reject) {
            api.deleteProduct(productId)
                .then(response => {
                    console.log("API call was successful: Delete product.");
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error(`Error deleting product with ID: ${productId}`));
                });
        });
    },
    updateProduct(productId, updatedProductData) {
        return new Promise(function (resolve, reject) {
            api.updateProductById(productId, updatedProductData)
                .then(response => {
                    console.log("API call was successful: Update product.");
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error updating product data."));
                });
        });
    }
};
