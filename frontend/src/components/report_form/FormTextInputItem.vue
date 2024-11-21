<!-- 
Component for text input and section header
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {ref} from 'vue'
    const props = defineProps(['sectionHeader', 'optionsList', 'selectionVar', 'selectField']);
    const confirmationModel = defineModel();
    const localSelectionVar = ref();
</script>
<template>
    <div class="text-input-container">
        <h3 class="section-header">{{ sectionHeader }}</h3>
        <input class="text-input" type="text" v-model="confirmationModel"/>
    </div>
</template>
<style scoped>
    .text-input-container {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 40%;
        min-width: 505px;
        background-color: transparent;
        margin-bottom: var(--form-element-spacing);
        margin-top: 0rem;
    }

    .text-input {
        border: 1pt solid var(--light-gray-outline);
        border-radius: 5px;
        height: 2.5rem;
        width: 100%;
        color: var(--dark-gray-text);
        font-weight: 500;
        font-size: var(--body-text-size);
        padding-left: .3rem;
    }

    .text-input:focus {
        border: var(--input-focus-border);
        outline: var(--input-focus-outline);
        transition: 0.03s;
    }

    .section-header {
        color: var(--dark-gray-text);
        font-size: var(--subheading-size);
        font-weight: var(--subheading-weight);
        line-height: var(--subheading-size);
        text-align: left;
        text-justify: top;
        margin-bottom: 0.25rem;
    }
</style>