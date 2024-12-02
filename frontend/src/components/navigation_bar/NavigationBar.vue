<!-- 
Component for the navigation bar shown on the top of the page
Last edited by: Nicholas Tullbane
Date: 11/25/24
-->
<script setup>
    import NavigationButton from './NavigationButton.vue';
    import {useRouter} from 'vue-router'
    import {ref, reactive} from 'vue'

    const router = useRouter();

    var homeIsActive = ref(true);
    var homeIsStandard = ref(false);
    const homeClassObject = reactive({
        active: homeIsActive,
        standard: homeIsStandard,
        'nav-button': true
    });

    var pathogenIsActive = ref(false);
    var pathogenIsStandard = ref(true);
    const pathogenClassObject = reactive({
        active: pathogenIsActive,
        standard: pathogenIsStandard,
        'nav-button': true
    });

    var reagentIsActive = ref(false);
    var reagentIsStandard = ref(true);
    var reagentClassObject = reactive({
        active: reagentIsActive,
        standard: reagentIsStandard,
        'nav-button': true
    });

    const flaskExampleIsActive = ref(false);
    const flaskExampleIsStandard = ref(true);
    const flaskExampleClassObject = reactive({
        active: flaskExampleIsActive,
        standard: flaskExampleIsStandard,
        'nav-button': true
    });

    const accountIsActive = ref(false);
    const accountIsStandard = ref(true);
    const accountClassObject = reactive({
        active: accountIsActive,
        standard: accountIsStandard,
        'nav-button': true
    });

    const signoutIsActive = ref(false);
    const signoutIsStandard = ref(true);
    const signoutClassObject = reactive({
        active: signoutIsActive,
        standard: signoutIsStandard,
        'nav-button': true
    });
    
    const oligoIsActive = ref(false);
    const oligoIsStandard = ref(true);
    const oligoClassObject = reactive({
        active: oligoIsActive,
        standard: oligoIsStandard,
        'nav-button': true
    });
    

    function navigateToPage(path, buttonName){
        console.log(path);
        if(path !== undefined){
            router.push(path);
        }
        homeIsActive.value = buttonName === 'home-nav';              // Changed some of these to 3 ='s
        pathogenIsActive.value = buttonName === 'pathogens-nav';
        reagentIsActive.value = buttonName === 'reagents-nav';
        flaskExampleIsActive.value = buttonName === 'flaskExample-nav';
        accountIsActive.value = buttonName === "accounts-nav"
        signoutIsActive.value = buttonName === "signout-nav"
        oligoIsActive.value = buttonName === "oligos-nav"
        

        homeIsStandard.value = buttonName !== 'home-nav';
        pathogenIsStandard.value = buttonName !== 'pathogens-nav';
        reagentIsStandard.value = buttonName !== 'reagents-nav';
        flaskExampleIsStandard.value = buttonName !== 'flaskExample-nav';
        accountIsStandard.value = buttonName !== 'accounts-nav';
        oligoIsStandard.value = buttonName !== 'oligos-nav';
    }
</script>

<template>
    <div class="nav-bar">
        <div id="navbar-logo">
            <img id="fwdx-image" src="@/assets/bioblade.svg" />
        </div>
        <div id="navbar-main-buttons">
            <NavigationButton text="Home" :class-object="homeClassObject" routerPath="/reports" button-name="home-nav" @nav-button-clicked="navigateToPage"/>
            <NavigationButton text="Pathogens" :class-object="pathogenClassObject" routerPath="/pathogens" button-name="pathogens-nav" @nav-button-clicked="navigateToPage"/>
            <NavigationButton text="Oligos" :class-object="oligoClassObject" routerPath="/oligos" button-name="oligos-nav" @nav-button-clicked="navigateToPage"/>
            <NavigationButton text="Products" :class-object="reagentClassObject" routerPath="/reagents" button-name="reagents-nav" @nav-button-clicked="navigateToPage"/>
<!--            <NavigationButton text="Flask Example" :class-object="flaskExampleClassObject" routerPath="/flaskExample" button-name="flaskExample-nav" @nav-button-clicked="navigateToPage"/>-->
        </div>
        <div id="navbar-account-buttons">
            <NavigationButton text="Sign Out" :class-object="signoutClassObject" routerPath="/" button-name="signout-nav" @nav-button-clicked="navigateToPage"/>
            <NavigationButton text="Account" :class-object="accountClassObject" router-path="/accounts" button-name="accounts-nav" @nav-button-clicked="navigateToPage" />
        </div>
    </div>
</template>

<style scoped>
    .nav-bar {
        padding: 0.25rem 1rem;
        /* background-color: #FFFFFF;
        border-bottom: 1pt solid #EFF0F1; */
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-bottom: 1pt solid #EFF0F1;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        color: #0E113E;
        font-family: 'Inter';
        height: 100%;
        max-height: 100%;
        min-height: 100%;
        min-width: 550px;
        position: sticky;
        top: 0;
        left: 0;
        z-index: 100;
    }

    @media(min-height: 1080px){
        #fwdx-image {
            width: auto;
            height: 65%;
            border-radius: 8px;
        }
    }

    @media(max-height: 1080px){
        #fwdx-image {
            width: 65%;
            height: auto;
            border-radius: 8px;
        }
    }

    @media(max-width: 900px){
        #fwdx-image {
            width: 100%;
            height: auto;
            border-radius: 8px;
            min-width: 100px;
        }
    }

    #navbar-logo {
        display: flex;
        flex-direction: row;
        justify-content: left;
        align-items: center;
        width: 20%;
        height: 100%;
        padding: 0;
    }

    #navbar-logo>h3 {
        font-size: clamp(9.5pt, 1.25vw, 12pt);
        font-weight: bold;
        text-wrap: nowrap;
    }

    #navbar-main-buttons {
        width: 60%;
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    #navbar-account-buttons {
        width: 20%;
        display: flex;
        flex-direction: row;
        justify-content: right;
        align-items: center;
    }
</style>