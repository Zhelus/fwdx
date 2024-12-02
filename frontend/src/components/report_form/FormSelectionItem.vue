<!-- 
Component for selection drop-down and section header
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {ref} from 'vue'

    const props = defineProps(['selectionHeader', 'optionsList', 'selectionVar', 'selectField', 'selectType']);
    const localSelectionVar = ref();
</script>
<template>
    <div class="selection-item-container">
        <!-- <p style="color: black;">{{ selectionVar.name }}</p> -->
        <h3 class="selection-header">{{ selectionHeader }}<span v-if="selectionVar === 'Test'" class="requirementMark">*</span></h3>
        <div class="table-selection-wrapper" v-if="selectType === 'table' && selectionVar !== 'Test'" @click="$emit('selectButtonClicked')">
            <p class="table-selection-display">
                {{ selectionVar.name }} 
            </p>
            <img class="table-select-img" src="../icons/edit-button-icon.svg"></img>
            <img class="table-select-img-hover" src="../icons/edit-button-yellow-icon.svg"></img>
            <!-- <button class="change-selection-button"></button> -->
        </div>
        <button v-if="selectType === 'table' && selectionVar === 'Test'" class="table-select-button" @click="$emit('selectButtonClicked')">
            Select {{ selectionHeader }}
        </button>
        <!-- <p v-if="selectionVar !== 'Test' && selectType === 'table'" class="selection-display">
            Selection: {{ selectionVar.name }} 
        </p> -->
        <!-- <div v-if="selectType === 'table'" class="select-button-wrapper" @click="$emit('selectButtonClicked')">
            <span v-if="selectionVar === 'Test'">Select {{ selectionHeader }}</span><span v-else>Change {{ selectionHeader }}</span>
        </div> -->
        <select v-if="selectType !== 'table'" class="select-box" v-model="localSelectionVar" @change="$emit('selectionChanged', localSelectionVar, selectField)">
            <option v-for="(option, index) in optionsList" :value="option.value" :key="index">{{ option.name }}</option>
        </select>
        <!-- <button v-if="selectionVar === 'Test' && selectionHeader === 'Pathogen'" class="select-button" @click="$emit('selectButtonClicked')">Select {{ selectionHeader }}</button> -->
    </div>
</template>
<style scoped>
    .requirementMark {
        color: var(--fwdx-yellow);
        font-size: var(--subheading-size);
        line-height: 0em;
        font-weight: 800;
        margin-left: 0.1em;
    }

    .table-select-button, .table-selection-wrapper {
        /* width: 12rem; */
        height: 2rem;
        padding: 0.5rem;
        border-radius: 5px;
        background-color: white;
        border-radius: 5px;
        outline: 1pt solid var(--light-gray-outline);
        min-width: 8.5rem;
    }

    .table-select-button, .table-selection-display {
        font-size: var(--body-text-size);
        color: var(--dark-gray-text);
    }

    .table-select-button {
        width: fit-content;
        border: none;
        width: 8.5rem;
        font-weight: 600;
    }

    .table-selection-display {
        font-weight: 500;
    }

    .table-select-button:hover, .table-selection-wrapper:hover {
        cursor: pointer;
        outline: 1.5pt solid var(--fwdx-yellow);
        transition: 0.05s;
    }

    .table-selection-wrapper:hover > .table-select-img {
        display: none;
        visibility: invisible;
    }

    .table-selection-wrapper:hover > .table-select-img-hover {
        display: block;
        visibility: visible;
        transition: 0.1s;
    }

    .table-selection-wrapper {
        display: flex;
        justify-content: space-between;
        align-items: center;
        column-gap: 0.5rem;
        width: fit-content;
    }

    .table-select-img, .table-select-img-hover {
        height: calc(var(--body-text-size) + 5pt);
    }

    .table-select-img-hover {
        display: none;
        visibility: invisible;
    }

    .selection-item-container {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 40%;
        min-width: 380px;
        background-color: transparent;
        margin-bottom: var(--form-element-spacing);
        margin-top: 0rem;
    }

    .selection-header {
        color: var(--dark-gray-text);
        font-size: var(--subheading-size);
        font-weight: var(--subheading-weight);
        line-height: var(--subheading-size);
        text-align: left;
        text-justify: top;
        margin-bottom: 0.25rem;
    }

    .selection-display {
        color: var(--dark-gray-text);
        font-size: var(--body-text-size);
        font-weight: 600;
    }

    .select-box {
        border: 1pt solid var(--light-gray-outline);
        border-radius: 5px;
        height: 2.5rem;
        width: 100%;
        color: var(--dark-gray-text);
        font-weight: 600;
        font-size: var(--body-text-size);
    }

    .select-box:focus {
        border: var(--input-focus-border);
        outline: var(--input-focus-outline);
    }

    .select-button {
        width: fit-content;
        text-align: left;
        height: auto;
        /* padding: 0.5em; */
        border: none;
        border-radius: 5px;
        background-color: var(--light-gray-outline);
        color: var(--fwdx-blue);
        font-size: var(--body-text-size);
        /* font-size: 0.9em; */
        font-weight: 600;
    }

    .select-button-wrapper {
        width: 10em;
        display: flex;
        justify-content: left;
        align-items: flex-start;
        text-align: left;
        height: auto;
        line-height: var(--body-text-size);
        color: var(--dark-gray-text);
        font-size: var(--body-text-size);
        font-weight: 500;
    }

    .select-button.inline {
        padding: 0.15em 0.5em;
        margin-left: 0.5em;
        background-color: var(--light-gray-button-hover);
        color: var(--fwdx-blue);
    }

    .select-button:hover {
        cursor: pointer;
        background-color: var(--light-gray-button-hover);
    }

    .select-button-wrapper:hover {
        cursor: pointer;
    }

    .select-button-wrapper:hover > span{
        color: var(--fwdx-yellow);
        font-weight: 700;
        transition: color 0.1s, font-weight 0.1s;
    }
</style>