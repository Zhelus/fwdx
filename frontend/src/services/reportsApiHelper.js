import api from "@/services/apiClient.js";

export default {
    getReport(id) {
        return new Promise(function(resolve, reject){
            api.getReportById(id)
                .then(response => {
                    console.log("API call was successful.");
                    console.log(response.data);
                    let reportJson = response.data['report'];
                    resolve(reportJson);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error(`Error fetching report with id: ${id}`));
                });
        });
    },
    getAllReports() {
        return new Promise(function(resolve, reject){
            api.getAllReports()
                .then(response => {
                    console.log("Successful API call -- get all reports.");
                    console.log(response.data);
                    let reportsData = response.data['reports'];
                    resolve(reportsData);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject("Error fetching all reports");
                });
        });
    },
    saveNewReport(report) {
        return new Promise(function(resolve, reject){
            const reportJson = report.getJson();
            api.createReport(reportJson)
                .then(response => {
                    console.log("API call was successful.");
                    resolve(response.data);
                })
                .catch(error => {
                    console.error("API call failed:", error);
                    reject(Error("Error creating new report."));
                });
        });
    }
}