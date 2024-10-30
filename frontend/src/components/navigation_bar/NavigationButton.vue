<!-- 
Component for navigation buttons contained in the navigation bar
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    import {useRouter} from 'vue-router'
    import {ref, computed, reactive} from 'vue'

    const props = defineProps(['text', 'classObject', 'routerPath', 'buttonName']);
    const router = useRouter();
</script>

<template>
    <button :class="classObject" @click="$emit('navButtonClicked', routerPath, buttonName)">{{ text }}</button>
</template>

<style scoped>
    button {
        color: var(--fwdx-blue);
        height: 2rem;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        font-size: clamp(8.5pt, 1.1vw, 10.5pt);
    }

    button:hover {
        cursor: pointer;
    }

    .nav-button {
        margin-top: 0;
        margin-bottom: 0;
        margin-left: min(0.4rem, 1%);
        margin-right: min(0.4rem, 1%);
        width: min(5.5rem, 11.5%);
    }

    .nav-button.standard:hover {
        background-color: var(--light-gray-button-hover);
        transition: background-color 0.2s;
    }

    .nav-button:active {
        background-color: #E3E3E3;
    }

    .nav-button.active {
        background-color: var(--light-gray-active-button);
    }

    .nav-button.active:hover {
        background-color: var(--light-gray-active-button);
    }

    .nav-button.standard {
        background-color: #FFFFFF;
    }

    .sign-out-button {
        margin-right: 1rem;
        background-color: #E3E3E3;
        width: clamp(60px, 35%, 80px);
    }

    .sign-out-button:hover {
        background-color: #DBDBDB;
        transition: background-color 0.2s;
    }

    .my-account-button {
        background-color: #0E113E;
        color: var(--fwdx-yellow);
        width: clamp(60px, 35%, 5rem);
        min-width: 60px;
    }

    .my-account-button:hover {
        background-color: var(--fwdx-blue);
        transition: background-color 0.2s;
    }
</style>