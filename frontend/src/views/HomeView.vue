<!-- 
Page view for the home page showing basic report information and actions
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import Card from '@/components/home_page/Card.vue'
    import ActionPane from '@/components/home_page/ActionPane.vue';
    import UpcomingCard from '@/components/home_page/UpcomingCard.vue';
    import {useRouter} from 'vue-router'
    
    const router = useRouter();

    function actionPaneClicked(path){
        if(path !== undefined){
            router.push(path);
        }
    }
</script>

<template>
<div class="generate-wrapper">
    <div class="new-reports-container">
        <div class="title-wrapper">
            <div class="container-ribbon-wrapper">
                <div class="container-ribbon blue-ribbon"></div>
            </div>
            <h4 class="container-title-text">New Reports</h4>
        </div>
        <Card report-id="1234567" card-title="RSV Report 3" card-type="report" pathogen-name="rsv" report-age="2 hours ago" pathogen-name-fmtd="RSV" reagent-name="Reagent #00123" mismatch-count="3"></Card>
        <Card report-id="1234567" card-title="Influenza Report 1" card-type="report" pathogen-name="influenza" report-age="2 days ago" pathogen-name-fmtd="Influenza" reagent-name="Reagent #00167" mismatch-count="0"></Card>
        <Card report-id="1234567" card-title="RSV Report 2" card-type="report" pathogen-name="rsv" report-age="2 weeks ago" pathogen-name-fmtd="RSV" reagent-name="Reagent #00123" mismatch-count="7"></Card>
    </div>
    <div class="scheduled-reports-container">
        <div class="scheduled-title-wrapper disabled">
            <div class="container-ribbon-wrapper">
                <div class="container-ribbon yellow-ribbon"></div>
            </div>
            <h4 class="container-title-text">Scheduled Reports (Coming Soon)</h4>
        </div>
        <div class="upcoming-cards-container">
            <UpcomingCard report-date="Oct. 25th" card-title="RSV Report" pathogen-name="RSV" reagent-name="Reagent #00123" report-frequency="Every 2 weeks" mismatch-count="25" />
            <UpcomingCard report-date="Oct. 26th" card-title="Influenza Report" pathogen-name="Influenza" reagent-name="Reagent #00167" report-frequency="Every 1 month" mismatch-count="8" />
            <UpcomingCard report-date="Oct. 29th" card-title="Covid-19 Report" pathogen-name="SARS-CoV-2" reagent-name="Reagent #00132" report-frequency="Every 1 week" mismatch-count="16" />
        </div>
    </div>
    <div class="actions-container">
        <div class="action-title-wrapper">
            <div class="container-ribbon-wrapper">
                <div class="container-ribbon gray-ribbon"></div>
            </div>
            <h4 class="container-title-text">Actions</h4>
        </div>
        <ActionPane action-name="Generate New Report" icon-name="lightning-icon" @click="actionPaneClicked('/reports/generate')"/>
        <!-- <ActionPane action-name="Schedule New Report" icon-name="schedule-icon" @click="actionPaneClicked('/reports/schedule')"/>
        <ActionPane action-name="Edit Existing Schedule" icon-name="pen-icon" @click="actionPaneClicked('/reports/schedule/edit')"/> -->
        <ActionPane action-name="Schedule New Report" icon-name="schedule-icon" disabled="true"/>
        <ActionPane action-name="Edit Existing Schedule" icon-name="pen-icon" disabled="true"/>
        <ActionPane action-name="Browse All Reports" icon-name="search-icon" @click="actionPaneClicked('/reports/browse')"/>
    </div>
</div>
</template>

<style>

.action-title-wrapper {
    grid-column: 1/3;
    grid-row: 1/2;
    width: 100%;
    height: 100%;
    background-color: var(--fwdx-white);
    border-radius: 6px 6px 0 0;
    padding: 3px;
    display: flex;
    align-items: center;
    box-shadow: 0 1px 0 0 var(--dark-box-shadow);
    min-width: 0;
    max-width: 100%;
}

.scheduled-title-wrapper {
    width: 100%;
    height: 100%;
    grid-row: 1/2;
    background-color: var(--fwdx-white);
    border-radius: 6px 6px 0 0;
    padding: 3px;
    display: flex;
    align-items: center;
    box-shadow: 0 1px 0 0 var(--dark-box-shadow);
    position: sticky;
    top: 0;
    left: 0;
}

.scheduled-title-wrapper.disabled {
    opacity: 0.5;
}

.placeholder {
    color: var(--fwdx-blue);
    font-weight: 500;
}


.generate-wrapper {
    display: grid;
    min-height: 750px;
    height: 100%;
    max-height: 100%;
    background-color: var(--gray-page-background);
    padding: 2rem;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 5fr 2.5fr 2.5fr;
    gap: 25px;
    min-width: 100%;
}

@media(max-width: 1200px) {
    .generate-wrapper-new {
        gap: 15px;
    }

    .upcoming-cards-container {
        min-width: 530px;
        padding-right: 10px;
    }
}

@media(max-height: 1080px) {
    .generate-wrapper-new {
        grid-template-rows: 5fr 2.5fr 2.5fr;
    }
}

@media(min-height: 1080px) {
    .generate-wrapper-new {
        grid-template-rows: 4fr 3fr 3fr;
    }
}

.new-reports-container{
    grid-column: 1;
    grid-row: 1 / 4;
    background-color: var(--light-gray-container-background);
    border-radius: 10px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    max-height: 100%;
    min-width: 360px;
}

.scheduled-reports-container{
    padding: 10px;
    grid-column: 2;
    grid-row: 1;
    background-color: var(--light-gray-container-background);
    border-radius: 10px;
    display: grid;
    grid-template-rows: 1fr 10fr;
    min-height: 0;
    grid-template-columns: 100%;
    max-height: 100%;
    gap: 10px;
    overflow-x: scroll;
    min-width: 0;

}

.upcoming-cards-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    width: 100%;
    min-height: 0;
    overflow-x: scroll;
}

.actions-container{
    min-height: 0;
    padding: 10px;
    grid-column: 2;
    grid-row: 2 / 4;
    background-color: var(--light-gray-container-background);
    border-radius: 10px;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: 1fr 5fr 5fr;
    gap: 10px;
    min-width: 0;
}

.title-wrapper {
    width: 100%;
    height: 4.5%;
    background-color: var(--fwdx-white);
    border-radius: 6px 6px 0 0;
    padding: 3px;
    display: flex;
    align-items: center;
    box-shadow: 0 1px 0 0 var(--dark-box-shadow);
}

.container-ribbon-wrapper {
    height: 100%;
    width: 12px;
    background-color: transparent;
}

.container-ribbon {
    transform: rotate(180deg);
    border-style: solid;
    border-width: 0px 0px 12px 12px;
    border-radius: 0 0 4px 0;
    height: 0px;
    width: 0px;
}

.blue-ribbon {
    border-color: transparent transparent var(--fwdx-blue) transparent;
}

.gray-ribbon {
    border-color: transparent transparent var(--light-gray-text) transparent;
}

.yellow-ribbon {
    border-color: transparent transparent var(--fwdx-yellow) transparent;
}

.container-title-text {
    margin-left: 6px;
    font-size: 16pt;
    font-weight: 600;
    color: var(--fwdx-blue); 
}
</style>