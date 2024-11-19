<script setup>
    const props = defineProps(['isLoading']);
</script>
<template>
    <div class="loader" v-if="!isLoading"></div>
</template>
<style scoped>
    .loader {
        position: absolute;
        top: 50%;
        left: 50%;
        margin-top: -120px;
        margin-left: -60px;
        border: 16px solid var(--light-gray-outline);
        border-top: 16px solid var(--fwdx-yellow);
        border-radius: 50%;
        width: 120px;
        height: 120px;
        animation: spin 0.75s ease-in-out infinite, changeColor 1.5s ease-in-out 0s infinite ;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes changeColor {
        0%     {
            /* background-color: var(--fwdx-yellow); */
            border-top: 16px solid var(--fwdx-blue); /* Blue */
        }
        50%  {
            /* background-color:var(--fwdx-white); */
            border-top: 16px solid var(--fwdx-yellow); /* Blue */
        }
        75%  {
            /* background-color:var(--fwdx-white); */
            border-top: 16px solid var(--fwdx-yellow); /* Blue */
        }
        100%{
            border-top: 16px solid var(--fwdx-blue); /* Blue */
        }
    }
</style>