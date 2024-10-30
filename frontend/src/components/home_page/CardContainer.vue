<script setup>
    const props = defineProps(['containerTitle', 'containerType'])
</script>
<template>
    <div class="card-container">
        <div class="title-wrapper">
            <div class="container-ribbon-wrapper">
                <div v-if="containerType === 'reports'" class="container-ribbon blue-ribbon"></div>
                <div v-if="containerType === 'schedule'" class="container-ribbon yellow-ribbon"></div>
            </div>
            <h4 class="container-title-text">{{ containerTitle }}</h4>
        </div>
        <div class="card-formatting">
           <slot></slot> 
        </div>
    </div>
</template>
<style scoped>
    .card-container {
        height: 85%;
        width: 25%;
        padding: 6px;
        background-color: #F7F7F7;
        border-radius: 8px;
    }

    .title-wrapper {
        width: 100%;
        height: 4.5%;
        background-color: #FFFFFF;
        border-radius: 6px 6px 0 0;
        padding: 3px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        box-shadow: 0 1px 0 0 rgba(0, 0, 0, 0.05);
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

    .yellow-ribbon {
        border-color: transparent transparent var(--fwdx-yellow) transparent;
    }

    .container-title-text {
        margin-left: 6px;
        font-size: 16pt;
        font-weight: 600;
        color: var(--fwdx-blue); 
    }

    .card-formatting {
        height: calc(95.5% - 10px);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
</style>