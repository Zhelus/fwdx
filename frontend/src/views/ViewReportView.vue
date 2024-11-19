<script setup>
    import MismatchDisplay from '@/components/view_report/MismatchDisplay.vue';
    import { onBeforeMount, onMounted, ref } from 'vue';
    import reportsApiHelper from '@/services/reportsApiHelper';
    import LoadingIcon from '@/components/misc/LoadingIcon.vue';


    const props = defineProps(['testProps']);
    // Get report data from MongoDB
    const reportData = ref({});
    const initComplete = ref(false);
    
    const mismatch = ref();
    mismatch.value = {
        oligoID: '67366cb26b5f81586e616809',
        oligoName: "Forward Primer",
        oligoSequence: 'AATGCAACAGTGCAATCTCA',
        mismatchLines: '|||||X||||||||||||||',
        pathogenSequence: 'AATGCCACAGTGCAATCTCA',
        pathogenAccessionID: 'KJ643523.1',
        pathogenCommonName: 'Respiratory syncytial virus type A',
        pathogenCollectionDate: '2015',
        pathogenLocation: 'USA',
        genomicPosition: '1987',
        mismatchIndex: [5],
        mismatchCount: 1
    }

    const mismatchTwo = ref();
    mismatchTwo.value = {
        oligoID: '67366cb26b5f81586e616809',
        oligoName: "Reverse Primer",
        oligoSequence: 'GGCCCAACACCAAATTCATC',
        mismatchLines: '||||XX||X||XX|XX|||X',
        pathogenSequence: 'GGCCTTACTCCTGAAACATA',
        pathogenAccessionID: 'MF001052.1',
        pathogenCommonName: 'Respiratory syncytial virus type A',
        pathogenCollectionDate: '2015',
        pathogenLocation: 'USA',
        genomicPosition: '708',
        mismatchIndex: [4, 5, 8, 11, 12, 14, 15, 19],
        mismatchCount: 8
    }

    const mismatchThree = ref();
    mismatchThree.value = {
        oligoID: '67366cb26b5f81586e616809',
        oligoName: "Probe 1",
        oligoSequence: 'AAACCTGCTTAGTTTCTTCTTGTTCTC',
        mismatchLines: '||||||||||||||||||||X|||||X',
        pathogenSequence: 'AAACCTGCTTAGTTTCTTCTGGTTCTT',
        pathogenAccessionID: 'MG027862.1',
        pathogenCommonName: 'Respiratory syncytial virus type A',
        pathogenCollectionDate: '2015',
        pathogenLocation: 'USA',
        genomicPosition: '3861',
        mismatchIndex: [21, 27],
        mismatchCount: 2
    }

    onBeforeMount(async () => {
        console.log("ON BEFORE MOUNT - VIEW REPORTS");
        console.log(props['testProps']);

        await reportsApiHelper.getReport(props.testProps)
            .then(data => {
                reportData.value = data;
                initComplete.value = true;
            })
            .catch(error => {
                console.error(error);
            })
    });
</script>
<template>
    <div class="page-wrapper">
        <LoadingIcon :init-complete="initComplete" />
        <div class="report-container"  v-if="initComplete" >
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
                <MismatchDisplay v-for="(x, index) in reportData.mismatches" :mismatch="x"/>
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