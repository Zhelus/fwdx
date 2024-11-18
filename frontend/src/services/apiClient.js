import axios from 'axios';

/*
Example apiClient file; eventually a real wrapper will need to be written.

Last edited by: Harrison Leath
Date: 10/30/24
 */

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:5000', // Flask server URL
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
});

export default {
    getDebug() {
        return apiClient.get('/v1/debug');
    },
    getPathogen() {
        return apiClient.get('/v1/pathogen/10632');
    },
    getReportById(reportId) {
        var url = '/v1/report/' + reportId;
        return apiClient.get(url);
    },
    createReport(reportData) {
        return apiClient.post('/v1/report', reportData)
    },
    updateReportById(reportId, updatedReportData) {
        var url = '/v1/report/' + reportId;
        return apiClient.put(url, updatedReportData)
    },
    deleteReport(reportId) {
        var url = '/v1/report/' + reportId;
        return apiClient.delete(url);
    },
    getAllReports() {
        var url = '/v1/report/all';
        return apiClient.get(url);
    },
    getAllProducts() {
        return apiClient.get('/v1/products');
    },
    getProductById(productId) {
        var url = '/v1/products/' + productId;
        return apiClient.get(url);
    },
    createProduct(productData) {
        return apiClient.post('/v1/products', productData);
    },
    updateProductById(productId, updatedProductData) {
        var url = '/v1/products/' + productId;
        return apiClient.put(url, updatedProductData);
    },
    deleteProduct(productId) {
        var url = '/v1/products/' + productId;
        return apiClient.delete(url);
    }, 
    getAllOligos() {
        return apiClient.get('/v1/oligos/all');
    },
    getActiveOligos() {
        return apiClient.get('/v1/oligos');
    },
    getOligoById(oligoId) {
        return apiClient.get(`/v1/oligos/${oligoId}`);
    },
    createOligo(oligoData) {
        return apiClient.post('/v1/oligos', oligoData);
    },
    archiveOligo(oligoId) {
        return apiClient.delete(`/v1/oligos/${oligoId}/archive`);
    }
};