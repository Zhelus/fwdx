<!-- 
Component for report-related actions on the home page
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import { ref } from 'vue'
    const props = defineProps(['actionName', 'iconName', 'disabled'])

    const classString = ref("action")
    if(props.disabled){
        classString.value += " disabled"
    }

    function getImageUrl() {
        console.log(props.iconName);
        return new URL(`../icons/${props.iconName}.svg`, import.meta.url)
    }
</script>
<template>
    <div :class="classString">
        <img class="action-icon" :src="getImageUrl()"></img>
        <h2 class="action-text">{{ actionName }}</h2>
        <h2 v-if="disabled" class="action-text small">(Coming Soon)</h2>
    </div>
</template>
<style scoped>
.action-icon {
    /* width: clamp(35px, 25%, 120px); */
    width: auto;
    height: 70%;
    margin-bottom: 0.2em;
}

.action-text {
    color: var(--fwdx-blue);
    font-weight: 500;
    font-size: clamp(9pt, 1.5vw, 16pt);
}

.action-text.small {
    font-size: clamp(6pt, 1vw, 11pt);
}

.action {
    background-color: #FFFFFF;
    padding: 30px 15px;
    border-radius: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 0;
    min-width: 140px;
    text-wrap: nowrap;
}

.action.disabled {
    opacity: 0.5;
}

.action:hover {
    cursor: pointer;
    outline: var(--light-gray-outline) solid 1.5pt;
    transition: outline 0.1s;
}

.action.disabled:hover{
    cursor: default;
    outline: none;
}
</style>