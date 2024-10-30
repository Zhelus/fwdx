<script setup>
    import {ref} from 'vue'

    const props = defineProps(['sectionHeader', 'optionsList', 'selectionVar', 'selectField']);
</script>
<template>
    <div class="checkbox-item-container">
        <h3 class="section-header">{{ sectionHeader }}</h3>
        <div class="checkboxes-container">
            <div v-for="(option, index) in optionsList" class="checkbox-wrapper">
                <input class="form-checkbox" type="checkbox" :value="option.value" :name="option.name + index">
                <label class="checkbox-label" :for="option.name + index">{{ option.name }}</label>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .checkbox-item-container {
        display: flex;
        flex-direction: column;
        height: 12%;
        width: 40%;
        min-width: 365px;
        background-color: transparent;
        margin-bottom: 2.5rem;
        margin-top: 0rem;
    }

    .checkboxes-container {
        display: flex;
        flex-wrap: wrap;
        height: 100%;
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

    .checkbox-wrapper {
        width: 33%;
        height: 22%;
        background-color: transparent;
        display: flex;
        justify-content: flex-start;
        align-items: flex-end;
        padding: 0;
    }


    /* input[type="checkbox"]{
        border: 1pt solid blue;
        outline: none;
    } */

    .form-checkbox {
        -webkit-appearance: none;
        -moz-appearance: none;
        appearance: none;
        height: 1.5vh;
        width: 1.5vh;
        outline: 0;
        border: 1px solid var(--light-gray-outline);
        border-radius: 2px;
        background-color: var(--fwdx-white);
    }

    .form-checkbox:hover {
        cursor: pointer;
        border: 1px solid var(--fwdx-yellow);
    }

    .form-checkbox:checked {
        -webkit-appearance: checkbox;
        -moz-appearance:checkbox;
        appearance: checkbox;
        /* border-radius: 3px;
        text-align: center;
        vertical-align: middle; */
        /* font-size: 1em; */
        /* accent-color: var(--fwdx-yellow); */
        accent-color: var(--fwdx-yellow);
        /* color: white; */
    }

    /* input[type='checkbox']:checked:after {
        content: '\2713';
        color:white;
        font-weight: 900;
    } */

    .checkbox-label {
        color: var(--dark-gray-text);
        margin-left: 0.25rem;
        font-size: 12pt;
        align-self: flex-end;
        line-height: 1em;
    }
</style>