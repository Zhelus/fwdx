<script setup>
    import {ref} from 'vue'

    const props = defineProps(['selectionHeader', 'optionsList', 'selectionVar', 'selectField']);
    const localSelectionVar = ref();
</script>
<template>
    <div class="selection-item-container">
        <h3 class="selection-header">{{ selectionHeader }}</h3>
        <select class="select-box" v-model="localSelectionVar" @change="$emit('selectionChanged', localSelectionVar, selectField)">
            <option v-for="(option, index) in optionsList" :value="option.value" :key="index">{{ option.name }}</option>
        </select>
    </div>
</template>
<style scoped>
    .selection-item-container {
        display: flex;
        flex-direction: column;
        height: auto;
        width: 40%;
        background-color: transparent;
        margin-bottom: 2.5rem;
        margin-top: 0rem;
    }

    .selection-header {
        color: var(--dark-gray-text);
        font-size: 16pt;
        font-weight: 700;
        line-height: 24px;
        text-align: left;
        text-justify: top;
        margin-bottom: 0.25rem;
    }

    .select-box {
        border: 1pt solid var(--light-gray-outline);
        border-radius: 5px;
        height: 2.5rem;
        width: 100%;
        color: var(--dark-gray-text);
        font-weight: 500;
        font-size: 12pt;
    }

    .select-box:focus {
        outline: 1pt solid var(--fwdx-yellow);
    }
</style>