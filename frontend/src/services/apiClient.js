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
    }
};