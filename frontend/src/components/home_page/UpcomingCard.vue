<!-- 
Component for displaying upcoming reports on the home page
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    const props = defineProps(['cardTitle', 'scheduleId', 'reportFrequency', 'pathogenName', 'reagentName', 'mismatchCount', 'reportDate'])
</script>
<template>
    <div class="card-wrapper">
        <div class="card-text">
            <div class="card-header">
                <h4 class="card-date">{{reportDate}}</h4>
                <div class="card-seperator yellow"></div>
                <h4 class="card-title">{{ cardTitle }}</h4>
            </div>
            <div class="card-details">
                <div class="card-info-wrapper">
                    <img class="inline-icon" src="../icons/clock-icon.svg"></img>
                    <p class="card-info">{{ reportFrequency }}</p>
                </div>
                <div class="card-info-wrapper">
                    <img class="inline-icon" src="../icons/virus-icon.svg"></img>
                    <p class="card-info">{{ pathogenName }}</p>
                </div>
                <div class="card-info-wrapper">
                    <img class="inline-icon" src="../icons/beaker-icon.svg"></img>
                    <p class="card-info">{{ reagentName }}</p>
                </div>
                <div class="card-info-wrapper">
                    <img class="inline-icon" src="../icons/mismatch-icon.svg"></img>
                    <p class="card-info">{{mismatchCount}} total mismatches</p>
                </div>
            </div>
        </div>
        <button class="card-button edit-schedule-button">Edit</button>
        <slot></slot>
    </div>
</template>
<style scoped>

    .card-wrapper {
        height: 100%;
        max-height: 100%;
        min-height: 0;
        width: 30%;
        min-width: 165px;
        padding: 10px;
        background-color: #FFFFFF;
        border-radius: 6px;
        display: grid;
        grid-template-rows: 9fr 1fr;
        grid-template-columns: 1fr;
        text-wrap: nowrap;
    }

    .card-info-wrapper {
        height: 12pt;
        width: 100%;
        display: flex;
        justify-content: left;
        align-items: center;
        margin-top: 12px;
        margin-bottom: 12px;
        min-height: 0;

    }

    @media(max-height: 1200px) {
        .card-info-wrapper {
            height: 7pt;
        }
    }

    @media(max-height: 900px) {
        .card-details {
            justify-content: center;
        }
    }

    @media(min-height: 900px) {
        .card-details {
            justify-content: flex-start;
            margin-top: 10px;
        }
    }

    @media(max-height: 1080px) {
        .inline-icon {
            height: 11pt;
            max-height: 11pt;
            width: auto;
            margin-right: 4pt;
        }

        .card-seperator {
            margin: 10px 0;
        }

    }

    @media(min-height: 1080px) {
        .inline-icon {
            height: 14pt;
            width: auto;
            margin-right: 4pt;
            min-height: 0;
            max-height: 14pt;
        }

        .card-seperator {
            margin: 10px 0;
        }

    }
    
    .card-text {
        grid-row: 1;
        grid-column: 1;
        height: 100%;
        width: 100%;
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 2.75fr 7.25fr;
        min-height: 0;
        max-height: 100%;
    }

    .card-header {
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: left;
    }

    .card-title {
        font-size: 14pt;
        font-weight: 500;
        color: var(--fwdx-blue); 
        line-height: 14pt;
    }

    .card-date {
        font-size: 18pt;
        font-weight: 600;
        color: var(--fwdx-blue); 
        line-height: 24pt;
    }

    .card-seperator {
        width: 60%;
        min-width: clamp(60%, calc(18pt * 6), 90%);
        max-width: calc(18pt * 6);
        height: 5px;
        border-radius: 3px;
    }

    .card-seperator.yellow {
        background-color: var(--fwdx-yellow);
    }

    .card-details {
        min-height: 0;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: left;
        overflow-x: scroll;
    }

    .card-info {
        color: var(--light-gray-text);
        font-size: clamp(9pt, 20%, 11pt);
    }

    .card-button {
        grid-row: 2;
        grid-column: 1;
        border-radius: 4px;
        width: 100%;
        height: 100%;
        border: none;
        font-size: 11pt;
        font-weight: 700;
        min-height: 0;
        flex: 0 1 auto;
        max-width: 100%;
        min-width: 0;
    }

    .card-button:hover {
        cursor: pointer;
    }

    .edit-schedule-button {
        background-color: var(--fwdx-yellow);
        color: var(--yellow-button-text);
    }
</style>