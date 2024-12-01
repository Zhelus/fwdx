<script setup>
    import { useRouter } from 'vue-router';
    const props = defineProps(['returnUrl', 'displayWarning']);
    const router = useRouter();

    function returnToPage(){
        if(props.displayWarning){
            if(window.confirm("Are you sure you want to leave this page? Any unsaved changes will be lost")){
                console.log("GOOD ALERT")
                router.push(props.returnUrl);
            }
            else{
                return;
            }
        }
        else{
            console.log(props.returnUrl);
            router.push(props.returnUrl);
        }
    }
</script>
<template>
    <div class="return-button-wrapper" @click="returnToPage">
        &#11013;
    </div>
</template>
<style scoped>
    .return-button-wrapper {
        width: 1.5em;
        height: 1.5em;
        background-color: var(--light-gray-button-bg);
        border-radius: 5px;
        outline: 1pt solid var(--light-gray-outline);
        display: flex;
        justify-content: center;
        align-items: center;
        color: var(--fwdx-blue);
        font-size: 12pt;
        font-weight: 500;
        margin: 0 0 1rem 0;
    }

    .return-button-wrapper:hover {
        cursor: pointer;
        background-color: var(--light-gray-button-hover);
    }
</style>