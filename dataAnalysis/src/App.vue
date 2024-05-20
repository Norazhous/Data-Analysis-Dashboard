<script>
import CanvasDrawing from './components/CanvasDrawing.vue'
import NavigationBar from './components/NavigationBar.vue'
import Consent from './components/Consent.vue'
import MeasuredDataFeedback from './components/MeasuredDataFeedback.vue'
import TableStudentCalculation from './components/TableStudentCalculation.vue'
import DataCompare from './components/DataCompare.vue'
import { RouterView } from 'vue-router'
import ping from './components/ping.vue'


export default {
  name: 'App',
  components: {
    NavigationBar,
    Consent,
    CanvasDrawing,
    MeasuredDataFeedback,
    TableStudentCalculation,
    DataCompare,
    ping,
  },
  data() {
    return {
      showConsentModal: false,
    }
  },
  computed: {
    
  },
  methods:{
   closeConsentModal(){
    this.showConsentModal =false;
   }
  }
}

</script>

<template>
  <router-view />
  <div id="app" class='container-fluid-sm m-0 background-white'>
    <navigation-bar @save="saveDataToLocalStorage" @toggleconsent="showConsentModal = true" />
    <consent v-if='showConsentModal' @consentset="closeConsentModal" />
    <MeasuredDataFeedback />
    <div class="row">
      <div class="col-lg-6">
        <CanvasDrawing />
      </div>
      <div class="col-lg-6">
        <TableStudentCalculation />
      </div>
      <div>
        <ping />
      </div>
    </div>
    <DataCompare />

  </div>
  <!-- <div class="row">
    <div class="col-6">
      <div>
        <h2> Enthalpy from students:</h2>
      </div>
      <CanvasDrawing />
      
    </div>
    <div class="col-6">
      <h2> Enthalpy from system:</h2>
      
      <img src="./assets/R134_p_h_diagram_with_cycle.svg" alt="" style="width: 550px; height: 400px;">

    </div>
  </div> -->

</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
<!-- 
<style scoped></style> -->
