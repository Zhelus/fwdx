<script setup>
    import MismatchDisplay from '@/components/view_report/MismatchDisplay.vue';
    import { onBeforeMount, onMounted, ref } from 'vue';
    import reportsApiHelper from '@/services/reportsApiHelper';
    import LoadingIcon from '@/components/misc/LoadingIcon.vue';


    const props = defineProps(['testProps']);
    // Get report data from MongoDB
    const reportData = ref({});
    const initComplete = ref(false);
    const oligoNames = ref([]);
    const oligoGroups = ref({});
    
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
        // await reportsApiHelper.getReport(props.testProps)
        //     .then(data => {
        //         reportData.value = data;
        //         initComplete.value = true;
        //     })
        //     .catch(error => {
        //         console.error(error);
        //     })

        reportData.value = {
            "_id": "673136062c3c0e7613ca1b9a",
            "report_id": "1234567",
            "schedule_id": "7654321",
            "report_title": "Test Report 1",
            "reagent_id": "6730f02aec38fbfe063398da",
            "pathogen_id": "10632",
            "mismatches":[
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Forward Primer",
                    "oligoSequence":"AATGCAACAGTGCAATCTCA",
                    "mismatchLines":"|||||X||||||||||||||",
                    "pathogenSequence":"AATGCCACAGTGCAATCTCA",
                    "pathogenAccessionID":"KJ643523.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "1987", 
                    "end_index": "2007",
                    "mismatchIndex":["5"],
                    "mismatchCount":"1"
                },
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Forward Primer",
                    "oligoSequence":"AATGCAACAGTGCAAGCTCATTT",
                    "mismatchLines":"|||||X|||||||||X||||XXX",
                    "pathogenSequence":"AATGCCACAGTGCAATCTCAGGG",
                    "pathogenAccessionID":"KJ643523.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "1987", 
                    "end_index": "2007",
                    "mismatchIndex":["5"],
                    "mismatchCount":"5"
                },
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Forward Primer",
                    "oligoSequence":"AATGCAACAGTGCAAGCTCATTT",
                    "mismatchLines":"|||||X|||||||||X||||XXX",
                    "pathogenSequence":"AATGCCACAGTGCAATCTCAGGG",
                    "pathogenAccessionID":"KJ643523.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "1987", 
                    "end_index": "2007",
                    "mismatchIndex":["5"],
                    "mismatchCount":"5"
                },
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Forward Primer",
                    "oligoSequence":"AATGCAACAGTGCAAGCTCATTT",
                    "mismatchLines":"|||||X|||||||||X||||XXX",
                    "pathogenSequence":"AATGCCACAGTGCAATCTCAGGG",
                    "pathogenAccessionID":"KJ643523.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "1987", 
                    "end_index": "2007",
                    "mismatchIndex":["5"],
                    "mismatchCount":"5"
                },
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Forward Primer",
                    "oligoSequence":"AATGCAACAGTGCAAGCTCATTT",
                    "mismatchLines":"|||||X|||||||||X||||XXX",
                    "pathogenSequence":"AATGCCACAGTGCAATCTCAGGG",
                    "pathogenAccessionID":"KJ643523.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "1987", 
                    "end_index": "2007",
                    "mismatchIndex":["5"],
                    "mismatchCount":"5"
                },
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Forward Primer",
                    "oligoSequence":"AATGCAACAGTGCAAGCTCATTTA",
                    "mismatchLines":"|||||X|||||||||X||||XXX|",
                    "pathogenSequence":"AATGCCACAGTGCAATCTCAGGGA",
                    "pathogenAccessionID":"KJ643523.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "1987", 
                    "end_index": "2007",
                    "mismatchIndex":["5"],
                    "mismatchCount":"5"
                },
                { 
                    "oligoID": "67366cb26b5f81586e616809", 
                    "oligoName": "Reverse Primer", 
                    "oligoSequence": "GGCCCAACACCAAATTCATC", 
                    "mismatchLines": "||||XX||X||XX|XX|||X", 
                    "pathogenSequence": "GGCCTTACTCCTGAAACATA", 
                    "pathogenAccessionID": "MF001052.1", 
                    "pathogenCommonName": "Respiratory syncytial virus type A", 
                    "pathogenCollectionDate": "2015", 
                    "pathogenLocation": "USA", 
                    "start_index": "708", 
                    "end_index": "728",
                    "mismatchIndex": ["4", "5", "8", "11", "12", "14", "15", "19"], 
                    "mismatchCount": "8" 
                },
                {
                    "oligoID":"67366cb26b5f81586e616809",
                    "oligoName":"Probe 1",
                    "oligoSequence":"AAACCTGCTTAGTTTCTTCTTGTTCTC",
                    "mismatchLines":"||||||||||||||||||||X|||||X",
                    "pathogenSequence":"AAACCTGCTTAGTTTCTTCTGGTTCTT",
                    "pathogenAccessionID":"MG027862.1",
                    "pathogenCommonName":"Respiratory syncytial virus type A",
                    "pathogenCollectionDate":"2015",
                    "pathogenLocation":"USA",
                    "start_index": "3861", 
                    "end_index": "3888",
                    "mismatchIndex":["21", "27"],
                    "mismatchCount": "2"
                }
            ],
            "creation_date":"11/15/24"
        }
        for(let x of reportData.value.mismatches){
            if(!oligoGroups.value[x.oligoName]){
                oligoGroups.value[x.oligoName] = [];
            }
            x["groupIndex"] = oligoGroups.value[x.oligoName].length;
            oligoGroups.value[x.oligoName].push(x);
        }
        initComplete.value = true;
    });
</script>
<template>
    <div class="page-wrapper">
        <LoadingIcon :init-complete="initComplete" />
        <div class="report-container"  v-if="initComplete" >
            <div class="report-header">
                <h1 class="report-title-text">{{ reportData.report_title }}</h1>
            </div>
            <!-- <div class="card-seperator blue"></div> -->
            <div class="report-stats">
                <h1 class="section-heading">Details</h1>
                <div class="details-section">
                    <img class="inline-icon" src="../components/icons/clock-icon.svg"></img>
                    <p class="details-text">{{reportData.creation_date}}</p>
                </div>
                <div class="details-section">
                    <img class="inline-icon" src="../components/icons/virus-icon.svg"></img>
                    <p class="details-text">{{reportData.pathogen_id}}</p>
                </div>
                <div class="details-section">
                    <img class="inline-icon" src="../components/icons/beaker-icon.svg"></img>
                    <p class="details-text">{{reportData.reagent_id}}</p>
                </div>
                <div class="details-section">
                    <img class="inline-icon" src="../components/icons/mismatch-icon.svg"></img>
                    <p class="details-text">{{reportData.mismatches.length}} total mismatches</p>
                </div>
            </div>
            <div class="report-mismatches">
                <h1 class="section-heading">Mismatches</h1>
                <!-- <MismatchDisplay v-for="(x, index) in reportData.mismatches" :mismatch="x"/> -->
                <MismatchDisplay v-for="(x, index) in oligoGroups" :mismatches="x"/>

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

    .details-section {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-start;
        height: auto;
    }

    .details-section:not(:last-child) {
        margin-bottom: 2pt;
    }

    .details-text {
        color: var(--dark-gray-text);
        font-size: var(--body-text-size);
    }

    .inline-icon {
        height: var(--body-text-size);
        width: auto;
        margin-right: 5pt;
        min-height: 0;
        max-height: 14pt;
    }

    .report-title-text {
        color: var(--fwdx-blue);
        font-weight: var(--page-header-weight);
        vertical-align: top;
        letter-spacing: -2%;
        font-size: var(--page-header-size);
        line-height: var(--page-header-line-height);
        /* margin-bottom: var(--form-header-margin); */
        margin-bottom: 0.5em;
    }

    .report-container {
        width: 100%;
        height: auto;
        /* background-color: var(--light-gray-container-background); */
        background-color: #fafafa;
        border-radius: 5px;
        padding: var(--form-padding);
        /* box-shadow: var(--container-box-shadow); */
        outline: 0.5pt solid var(--light-gray-outline);
    }

    .report-container > div:not(.card-seperator){
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

    .card-seperator {
        width: 15em;
        height: 5px;
        border-radius: 3px;
        background-color: var(--fwdx-blue);
        margin:  0 0 var(--form-header-margin) 0;
    }
</style>