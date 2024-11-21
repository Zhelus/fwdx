<!-- 
Component for performing actions with a form (submit, cancel, etc.)
Last edited by: Blake Good
Date: 10/30/24
-->
<script setup>
    const props = defineProps(['buttonText', 'buttonClass']);
    const emit = defineEmits(['submitButtonClicked', 'cancelButtonClicked']);
    const confirmationModel = defineModel();
</script>
<template>
    <button :class="buttonClass" @click="emit(`${buttonClass}ButtonClicked`)" :disabled="buttonClass == 'submit' && confirmationModel != 'YES'">{{ buttonText }}</button>
</template>
<style scoped>
    button {
        width: auto;
        min-width: 75px;
        font-size: var(--body-text-size);
        font-weight: var(--subheading-weight);
        border: none;
        border-radius: 5px;
        padding: 5px;
    }

    button:enabled:hover {
        cursor: pointer;
    }

    button.submit {
        background-color: var(--fwdx-blue);
        color: var(--blue-button-text);
    }

    button:disabled {
        opacity: var(--disabled-button-opacity);
    }

    button:disabled:hover {
        cursor: default;
    }

    button.submit:enabled:hover {
        background-color: var(--fwdx-blue-button-hover);
        transition: background-color 0.2s;
    }

    button.cancel {
        background-color: var(--light-gray-button-bg);
        color: var(--light-gray-button-text);
    }

    button.cancel:enabled:hover {
        background-color: var(--light-gray-button-hover);
        transition: background-color 0.2s;
    }
</style>