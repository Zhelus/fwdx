<script setup>
    const props = defineProps(['ncbiTaxonomyID', 'pathogenName', 'buttonClass'])
</script>
<template>
    <button :class="buttonClass" @click="$emit('addPathogenClicked', ncbiTaxonomyID, pathogenName)">Add</button>
</template>
<style scoped>
     @media(min-width: 1400px) {
        .card-button {
            width: 100px;
            height: 100%;
            font-size: 11pt;
            font-weight: 600;
            grid-column: 2;
        }
    }

    @media(max-width: 1400px) {
        .card-button {
            width: 50px;
            height: 80%;
            font-size: 10pt;
            font-weight: 600;
        }
    }

    .card-button {
        border-radius: 4px;
        border: none;
        background-color: var(--fwdx-blue);
        color: var(--blue-button-text);
    }

    .table-button {
        background-color: var(--fwdx-blue);
        color: var(--blue-button-text);
        border-radius: 5px;
        height: 25px;
        width: 60%;
        min-width: 50px;
        border: none;
        outline: none;
        font-size: 11pt;
        font-weight: 500;
    }

    button:hover {
        cursor: pointer;
        background-color: var(--fwdx-blue-button-hover);
    }
</style>