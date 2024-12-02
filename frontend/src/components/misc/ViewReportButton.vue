<script setup>
    import {useRouter} from 'vue-router'
    const router = useRouter();
    const props = defineProps(['reportId', 'buttonClass'])
    function viewReportClicked() {
        router.push({ name: 'viewReport', params: {testProps: props.reportId} });
    }
</script>
<template>
    <button :class="buttonClass" @click="viewReportClicked()">View</button>
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
        height: 1.6em;
        width: 3.2em;
        /* min-width: 50px; */
        border: none;
        outline: none;
        font-size: 10pt;
        font-weight: 700;
    }

    button:hover {
        cursor: pointer;
        background-color: var(--fwdx-blue-button-hover);
    }
</style>