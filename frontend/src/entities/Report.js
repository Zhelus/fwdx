import api from "@/services/apiClient.js";
class Report {
    // Constructor method used to create a new report
    constructor(reportId, reportTitle, scheduleId, reagentId, pathogenId, creationDate, mismatches){
        this.reportId = reportId;
        this.reportTitle = reportTitle;
        this.scheduleId = scheduleId;
        this.reagentId = reagentId;
        this.pathogenId = pathogenId;
        this.creationDate = creationDate;
        this.mismatches = mismatches;
    }

    // Translate the report data into JSON format. Used for sending report data to the backend
    getJson() {
        const reportJson = {
            'report_id': this.reportId,
            'report_title': this.reportTitle,
            'schedule_id': this.scheduleId,
            'reagent_id': this.reagentId,
            'pathogen_id': this.pathogenId,
            'creation_date': this.creationDate,
            'mismatches': this.mismatches
        };
        return reportJson;
    }

    // Save the report to MongoDB
    saveNewReport(){
        var responseData = ""
        const reportData = this.getJson();
        api.createReport(reportData)
            .then(response => {
                console.log("API call was successful.");
                responseData = response.data;
            })
            .catch(error => {
                console.error("API call failed:", error);
                responseData = "Error occurred while fetching data.";
            });
        console.log(responseData);
        return responseData;
    }

    // Update the report with new data
    updateReport(updatedReportData){
        var responseData = ""
        api.updateReportById(this.reportId, updatedReportData)
            .then(response => {
                console.log("API call was successful.");
                responseData = response.data;
            })
            .catch(error => {
                console.error("API call failed:", error);
                responseData = "Error occurred while fetching data.";
            });
        console.log(responseData);
        return responseData;
    }

    deleteReport() {
        var responseData = "";
        api.deleteReport(this.reportId)
            .then(response => {
                console.log("API call was successful.");
                responseData = response.data;
            })
            .catch(error => {
                console.error("API call failed:", error);
                responseData = "Error occurred while fetching data.";
            });
        console.log(responseData);
        return responseData;
    }
}

export default Report;