<script setup>
    import MismatchDisplay from '@/components/view_report/MismatchDisplay.vue';
    import { onBeforeMount, onMounted, ref } from 'vue';
    import reportsApiHelper from '@/services/reportsApiHelper';
    import LoadingIcon from '@/components/misc/LoadingIcon.vue';


    const props = defineProps(['testProps']);
    // Get report data from MongoDB
    const reportData = ref({});
    const pageIsLoading = ref(false);
    
    const mismatch = ref();
    mismatch.value = {
        primer: 'AATGCAACAGTGCAATCTCA',
        mismatchLines: '|||||X||||||||||||||',
        genomicSequence: 'AATGCCACAGTGCAATCTCA',
        genomicPosition: '1987',
        mismatchIndex: 5,
        mismatchCount: 1,
        name: "Forward Primer"
    }

    const mismatchTwo = ref();
    mismatchTwo.value = {
        primer: 'GGCCCAACACCAAATTCATC',
        mismatchLines: '||||XX||X||XX|XX|||X',
        genomicSequence: 'GGCCTTACTCCTGAAACATA',
        genomicPosition: '708',
        mismatchIndex: 5,
        mismatchCount: 8,
        name: "Reverse Primer"
    }

    const mismatchThree = ref();
    mismatchThree.value = {
        primer: 'AAACCTGCTTAGTTTCTTCTTGTTCTC',
        mismatchLines: '||||||||||||||||||||X|||||X',
        genomicSequence: 'AAACCTGCTTAGTTTCTTCTGGTTCTT',
        genomicPosition: '3861',
        mismatchIndex: 5,
        mismatchCount: 2,
        name: "Probe #1"
    }
    const mismatchPercentages = ref([]);

    onBeforeMount(async () => {
        console.log("ON BEFORE MOUNT - VIEW REPORTS");
        console.log(props['testProps']);

        await reportsApiHelper.getReport(props.testProps)
            .then(data => {
                reportData.value = data;
                pageIsLoading.value = true;
            })
            .catch(error => {
                console.error(error);
            })
    });
</script>
<template>
    <!-- <h1 style="color: var(--fwdx-blue);">{{ testProps }}</h1> -->
    <div class="page-wrapper">
        <LoadingIcon :is-loading="pageIsLoading" />
        <div class="report-container"  v-if="pageIsLoading" >
            <div class="report-header">
                <h1 class="report-title-text">{{ reportData.report_title }}</h1>
            </div>
            <div class="report-stats">
                <h1 class="section-heading">Details</h1>
                <p>Date</p>
                <p>Virus</p>
                <p>Reagent</p>
                <p>Mismatches</p>
            </div>
            <div class="report-mismatches">
                <h1 class="section-heading">Mismatches</h1>
                <MismatchDisplay :mismatch="mismatch"/>
                <MismatchDisplay :mismatch="mismatchTwo"/>
                <MismatchDisplay :mismatch="mismatchThree"/>
            </div>
        </div>
    </div>
</template>
<style scoped>
    .page-wrapper {
        color: var(--fwdx-blue);
        min-height: 100%;
        height: 100%;
        max-height: 100%;
        background-color: var(--gray-page-background);
        padding: 2rem;
        min-width: 100%;
        display: flex;
        justify-content: center;
        align-items: flex-start;
    }

    .section-heading {
        color: var(--dark-gray-text);
        font-size: var(--subheading-size);
        font-weight: var(--subheading-weight);
        line-height: var(--subheading-size);
        text-align: left;
        text-justify: top;
        margin-bottom: 0.25rem;
    }

    .report-title-text {
        color: var(--fwdx-blue);
        font-weight: var(--page-header-weight);
        vertical-align: top;
        letter-spacing: -2%;
        font-size: var(--page-header-size);
        line-height: var(--page-header-line-height);
        margin-bottom: var(--form-header-margin);
    }

    .report-container {
        width: 100%;
        height: auto;
        background-color: var(--light-gray-container-background);
        border-radius: 5px;
        padding: 25px;
        /* box-shadow: var(--container-box-shadow); */
        outline: 0.5pt solid var(--light-gray-outline);
    }

    .report-container > div{
        width: 100%;
    }

    .report-header {
        height: auto;
    }

    .report-stats{
        margin-bottom: var(--form-element-spacing);
    }

    .report-mismatches {
        height: auto;
    }


</style>