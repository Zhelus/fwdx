<script setup>
    import { ref, onMounted, onBeforeMount } from 'vue'

    const props = defineProps(['mismatch']);
    const sequenceCharClassName = ref("")
    // Set the size of each mismatch character
    onMounted(() => {
        console.log(props.mismatch);
        sequenceCharClassName.value = `${props.mismatch.oligoName.replaceAll(' ', '')}-sequence-char`
        let numChars = props.mismatch.oligoSequence.length;
        let widthPercentage = 100/numChars;
        let chars = document.getElementsByClassName(sequenceCharClassName.value);
        for(let i=0; i<chars.length; i++){
            chars[i].style.width = `${widthPercentage}%`;
        }
    })
</script>
<template>
    <div class="mismatch-container">
        <div class="mismatch-title-wrapper">
            <img class="inline-icon" src="../icons/dna-icon.svg"></img>
            <h3 class="mismatch-title">{{ mismatch.oligoName }}</h3>
        </div>
        <div class="mismatch-wrapper">
            <div class="sequence-wrapper fwdx-seq">
                <div :class="`sequence-char ${mismatch.oligoName.replaceAll(' ', '')}-sequence-char`" v-for="(x, index) in mismatch.oligoSequence">{{ x }}</div>
            </div>
            <div class="sequence-wrapper mismatch-seq">
                <div v-for="(x, index) in mismatch.mismatchLines" :class="[x=='|' ? 'matchSymbol' : 'mismatchSymbol', `sequence-char ${mismatch.oligoName.replaceAll(' ', '')}-sequence-char`]"><span>{{ x }}</span></div>
            </div>
            <div class="sequence-wrapper genomic-seq">
                <div :class="`sequence-char ${mismatch.oligoName.replaceAll(' ', '')}-sequence-char`" v-for="(x, index) in mismatch.pathogenSequence">{{ x }}</div>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .mismatch-container {
        width: 100%;
        height: auto;
    }

    .mismatch-container:not(:last-child) {
        margin-bottom: 2.5em;
    }

    .inline-icon {
        height: var(--body-text-size);
        margin-right: 0.4em;
    }

    .mismatch-title-wrapper{
        height: auto;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
        margin-bottom: 0.1em;
    }

    .mismatch-title {
        font-size: var(--body-text-size);
        font-weight: 600;
        color: var(--dark-gray-text);
    }

    .mismatch-wrapper{
        border-radius: 5px;
        width: 100%;
        max-width: 100%;
        overflow-x: scroll;
        border: 2pt solid var(--light-gray-outline);
        height: auto;
    }
    .sequence-wrapper {
        display: flex;
        justify-content: space-between;
        width: 100%;
    }

    .mismatch-seq {
        /* background-color: #f3f3f3; */
        /* height: 1.5em; */
        height: calc(1.5em + 2pt);
    }

    .mismatch-seq > .sequence-char {
        border-top: 1.5pt solid var(--light-gray-outline);
        border-bottom: 1.5pt solid var(--light-gray-outline);
    }

    .matchSymbol > span{
        font-weight: 900;
    }

    .mismatchSymbol > span {
        font-weight: var(--mismatch-body-weight);
    }

    .sequence-char.matchSymbol {
        color: #f3f3f3;
        background-color: var(--green-text);
        font-weight: var(--mismatch-body-weight);
        font-size: 8pt;
    }

    .sequence-char.mismatchSymbol {
        color: #f3f3f3;
        background-color: var(--red-text);
        font-weight: var(--mismatch-body-weight);
    }

    .genomic-seq, .fwdx-seq {
        background-color: white;
        height: 2em;
    }

    .genomic-seq>.sequence-char, .fwdx-seq>.sequence-char{
        background-color: white;
    }

    .fwdx-seq {
        border-top-left-radius: 5px;
        border-radius: 5px 5px 0 0;
    }

    .genomic-seq {
        border-radius: 0 0 5px 5px;
    }

    .sequence-char {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: transparent;
        font-size: var(--body-text-size);
        font-weight: 500;
        height: 100%;
        min-width: 32px;
    }

    .sequence-char:not(:last-child) {
        border-right: 2pt solid var(--light-gray-outline);
    }


</style>