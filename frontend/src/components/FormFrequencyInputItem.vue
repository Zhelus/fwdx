<!-- 
Component for inputting the frequency of a scheduled report
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {ref} from 'vue'
    const props = defineProps(['sectionHeader']);
    const localsectionVar = ref();

    function unitSelected(unitId){
        var units = document.getElementsByClassName('unit-option');
        for(let i=0; i<units.length; i++){
            if(units[i].id == unitId){
                units[i].classList.add('active');
            }
            else{
                units[i].classList.remove('active');
            }
        }
    }
</script>
<template>
    <div class="section-item-container">
        <h3 class="section-header">{{ sectionHeader }}</h3>
        <div class="frequency-input-wrapper">
            <input class="frequency-value-input" type="text" />
            <div class="frequency-unit-options">
                <div id="days-unit" class="unit-option" @click="unitSelected('days-unit')">Days</div>
                <div id="weeks-unit" class="unit-option" @click="unitSelected('weeks-unit')">Weeks</div>
                <div id="months-unit" class="unit-option" @click="unitSelected('months-unit')">Months</div>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .section-item-container {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 40%;
        min-width: 380px;
        background-color: transparent;
        margin-bottom: 2.5rem;
        margin-top: 0rem;
    }

    .section-header {
        color: var(--dark-gray-text);
        font-size: 16pt;
        font-weight: 700;
        line-height: 24px;
        text-align: left;
        text-justify: top;
        margin-bottom: 0.25rem;
    }

    .frequency-input-wrapper {
        display: grid;
        grid-template-columns: 1fr 2fr;
        grid-template-rows: 2.5rem;
        width: 100%;
        gap: 15px;
        /* font-size: 12pt; */
    }

    .frequency-value-input {
        height: 100%;
        width: 100%;
        border: 1pt solid var(--light-gray-outline);
        border-radius: var(--input-border-radius);
        color: var(--dark-gray-text);
        font-size: 12pt;
        padding-left: .3rem;
        background-color: var(--fwdx-white);
    }

    .frequency-value-input:focus {
        border: var(--input-focus-border);
        outline: var(--input-focus-outline);
    }

    .frequency-unit-options {
        height: 100%;
        width: 100%;
        color: var(--dark-gray-text);
        font-size: 12pt;
        background-color: var(--fwdx-white);
        outline: 1pt solid var(--light-gray-outline);
        display: grid;
        grid-template-rows: 100%;
        grid-template-columns: repeat(3, 1fr);
        border-radius: var(--input-border-radius);
    }

    .unit-option {
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .unit-option.active {
        color: var(--fwdx-white);
        font-weight: 800;
        background-color: var(--fwdx-yellow);
        transition: 0.1s;
    }

    .unit-option:not(.active):hover {
        cursor: pointer;
        background-color: var(--transparent-button-hover);
        transition: background-color 0.2s;
    }

    .unit-option:not(:first-child, :last-child){
        border-right: 1pt solid var(--light-gray-outline);
        border-left: 1pt solid var(--light-gray-outline);
    }

    .unit-option:first-child{
       border-top-left-radius: var(--input-border-radius);
       border-bottom-left-radius: var(--input-border-radius);
    }

    .unit-option:last-child{
       border-top-right-radius: var(--input-border-radius);
       border-bottom-right-radius: var(--input-border-radius);
    }
</style>