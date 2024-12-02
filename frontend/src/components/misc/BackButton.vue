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
        <!-- &#11013; -->
        <img class="back-icon" src="../icons/back-arrow-blue.svg"></img>

    </div>
</template>
<style scoped>
    .back-icon {
        width: auto;
        height: 100%;
    }

    .return-button-wrapper {
        width: 2.1em;
        height: 1.4em;
        min-height: 1.25em;
        /* background-color: var(--light-gray-button-bg); */
        background-color: white;
        /* outline: 0.5pt solid var(--light-gray-outline); */
        box-shadow: 0 1px 2.25px -1.5px var(--fwdx-blue);
        border-radius: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        color: var(--fwdx-blue);
        font-size: 12pt;
        font-weight: 500;
        margin: 0 0 0.5em 0;
    }

    .return-button-wrapper:hover {
        cursor: pointer;
        background-color: var(--light-gray-button-hover);
        transition: background-color 0.1s;
    }

    .return-button-wrapper:active {
        box-shadow: none;
    }
</style>