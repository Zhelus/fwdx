import axios from 'axios';

/*
Example apiClient file; eventually a real wrapper will need to be written.

Last edited by: Harrison Leath
Date: 10/30/24
 */

const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:5000', // Flask server URL
    withCredentials: true,            // Changed to true since we are using sessions
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
    getUser(user_id) {
        var url = 'v1/users/get/' + user_id;
        return apiClient.get(url)
    },
    getAllUsers(){
        var url = 'v1/users/get_all_users'
        return apiClient.get(url)
    },
    updateUser(user_id, user_data) {
        var url = 'v1/users/update/' + user_id;
        return apiClient.put(url, user_data)
    },
    deleteUser(user_id){
        var url = 'v1/users/delete/' + user_id;
        return apiClient.delete(user_id)
    },
    loginUser(credentials){
        var url = 'v1/users/login';
        return apiClient.post(url, credentials)
    },
    logoutUser(user_id){
        var url = 'v1/users/logout/' + user_id;
        return apiClient.post(url)
    },
    registerUser(){
        var url = 'v1/users/register';
        return apiClient.post(url)
    }


};