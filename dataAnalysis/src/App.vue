<script>
import CanvasDrawing from './components/CanvasDrawing.vue'
import NavigationBar from './components/NavigationBar.vue'
import Consent from './components/Consent.vue'
import Streams from './components/Streams.vue'
import MeasuredDataFeedback from './components/MeasuredDataFeedback.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    Streams,
    Consent,
    CanvasDrawing,
    MeasuredDataFeedback,
  },
  data() {
    return {
        showConsentModal: false,
    }
  },
}

</script>

<template>
  <div id="app" class='container-fluid-sm m-0 background-white'>
    <navigation-bar @save="saveDataToLocalStorage" @toggleconsent="showConsentModal = true"/>
    <consent v-if='showConsentModal' @consentset="closeConsentModal"/>
    <MeasuredDataFeedback/>


</div>
  <div class="row">
    <div class="col-6">
      <div>
        <h2> Enthalpy from students:</h2>
      </div>
      <CanvasDrawing />
      <!-- <div>
        <h3>
          Student Data Record
        </h3>
      </div>
      <div id="record">
        <table class="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">T1</th>
            <th scope="col">T2</th>
            <th scope="col">P1</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>10</td>
            <td>60</td>
            <td>40</td>
          </tr>
        </tbody>
      </table>
      </div> -->
      
    </div>
    <div class="col-6">
      <h2> Enthalpy from system:</h2>
      
      <img src="./assets/R134_p_h_diagram_with_cycle.svg" alt="" style="width: 550px; height: 400px;">
      <!-- <div>
        <h3>
          System Result
        </h3>
        <span>
          h1 = 408225.86333931104
        </span>
        <br>
        <span>
          h2 = 442579.31506051804
        </span>
        <br>
        <span> h3 = 258654.52071279605
          <br>
          h4 = 400368.5914600562
          <br>
          h5 = 399650.00016082387
          <br>
          Q = 209.399879677121
          <br>
          p_l = 1058110.330234713 p_v = 307947.7425995305 T_v= 0.6720637378023184 T_l 41.2104928329764
        </span>
      </div>
    </div>
    <div> -->

    </div>
  </div>
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
