<!-- 
Component for cards showing newest reports on home page
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    const props = defineProps(['cardTitle', 'cardType', 'pathogenName', 'reportId', 'reportAge', 'pathogenNameFmtd', 'reagentName', 'mismatchCount'])
    import {useRouter} from 'vue-router'
    import ViewReportButton from '../misc/ViewReportButton.vue';
    const router = useRouter();

    function getImageUrl() {
        return new URL(`./card_images/${props.pathogenName}.jpg`, import.meta.url)
    }
</script>
<template>
    <div class="card-wrapper">
        <div class="card-image-wrapper">
            <img class="card-image" :src="getImageUrl()"> 
        </div>
        <div class="card-details">
            <h4 class="card-title">{{ cardTitle }}</h4>
            <div v-if="cardType === 'report'" class="card-seperator blue"></div>
            <div v-if="cardType === 'schedule'" class="card-seperator yellow"></div>
            <div class="card-bottom-bar">
                <div class="card-info-wrapper">
                    <div class="info-container">
                        <img class="inline-icon" src="../icons/clock-icon.svg"></img>
                        <p class="card-info">{{ reportAge }}</p>
                    </div>
                    <div class="info-container">
                        <img class="inline-icon" src="../icons/virus-icon.svg"></img>
                        <p class="card-info">{{ pathogenNameFmtd }}</p>
                    </div>
                    <div class="info-container">
                        <img class="inline-icon" src="../icons/beaker-icon.svg"></img>
                        <p class="card-info">{{ reagentName }}</p>
                    </div>
                    <div class="info-container">
                        <img class="inline-icon" src="../icons/mismatch-icon.svg"></img>
                        <p class="card-info">{{ mismatchCount }} total mismatches</p>
                    </div>
                </div>
                <ViewReportButton v-if="cardType === 'report'" button-class="card-button" :report-id="reportId" />
                <button v-if="cardType === 'schedule'" class="card-button edit-schedule-button">Edit</button>
            </div>
        </div>
        <slot></slot>
    </div>
</template>
<style scoped>
    @media(max-width: 1000px){
        .card-info-wrapper {
            visibility: hidden;
        }
    }

    @media(min-width: 1400px) {
        .info-container {
            display: flex;
            justify-content: left;
            align-items: center;
        }

        .card-info-wrapper {
            height: 12pt;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 600px;
        }

        .inline-icon {
            height: 12pt;
            width: auto;
            margin-right: 4pt;
            min-height: 0;
            max-height: 14pt;
        }
        
        .card-info {
            color: var(--light-gray-text);
            font-size: clamp(10pt, 40%, 14pt);
        }

        .card-button {
            width: 100px;
            height: 100%;
            font-size: 11pt;
            font-weight: 600;
            grid-column: 2;
        }

        .card-bottom-bar {
            width: 100%;
            height: 30px;
            display: grid;
            grid-template-rows: 1fr;
            grid-template-columns: 1fr 100px;
            gap: 50px;
        }
    }

    @media(max-width: 1400px) {
        .info-container {
            display: flex;
            justify-content: left;
            align-items: center;
        }

        .card-info-wrapper {
            height: 12pt;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 600px;
        }

        .inline-icon {
            height: 9.5pt;
            width: auto;
            margin-right: 1pt;
            min-height: 0;
            max-height: 14pt;
        }
        
        .card-info {
            color: var(--light-gray-text);
            font-size: 9pt;
        }

        .card-button {
            width: 50px;
            height: 80%;
            font-size: 10pt;
            font-weight: 600;
        }

        .card-bottom-bar {
            width: 100%;
            height: 30px;
            display: grid;
            grid-template-rows: 1fr;
            grid-template-columns: 1fr 50px;
            gap: 25px;
        }
    }



    .card-wrapper {
        max-height: 30%;
        width: 100%;
        padding: 10px;
        background-color: #FFFFFF;
        border-radius: 6px;
        flex: 0 1 30%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }

    .card-image-wrapper {
        background-size: cover;
        width: 100%;
        height: 55%;
        border-radius: 4px;
    }

    .card-image-wrapper::before {
        background-color: var(--fwdx-yellow);
        border-radius: 4px;
        content: '';
        display: block;
        width: 100%;
        height: 100%;
        mix-blend-mode: darken;
        position: relative;
        top: 0;
        left: 0;
    }

    .card-image-wrapper::after {
        background-color: var(--fwdx-blue);
        border-radius: 4px;
        content: '';
        display: block;
        width: 100%;
        height: 100%;
        mix-blend-mode: lighten;
        position: relative;
        top: calc(-200% + -6px);
        left: 0;
    }

    .card-image {
        width: 100%;
        height: 100%;
        border-radius: 4px;
        object-fit: cover;
        filter: grayscale(100%) contrast(1) blur(0px);
        mix-blend-mode: multiply;
        opacity: 1;
        position: relative;
        top: -100%;
        left: 0;
    }

    .card-details {
        width: 100%;
        height: 40%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    .card-title {
        font-size: 16pt;
        font-weight: 500;
        color: var(--fwdx-blue); 
    }

    .card-seperator {
        width: 20%;
        height: 5px;
        border-radius: 3px;
    }

    .card-seperator.blue {
        background-color: var(--fwdx-blue);
    }

    .card-seperator.yellow {
        background-color: var(--fwdx-yellow);
    }

    .card-bottom-bar {
        width: 100%;
        height: 30px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
    }

    .card-time-stats {
        color: var(--light-gray-text)
    }

    .card-button {
        border-radius: 4px;
        border: none;
    }

    .card-button:hover {
        cursor: pointer;
    }

    .edit-schedule-button {
        background-color: var(--fwdx-yellow);
        color: var(--yellow-button-text);
    }
</style>