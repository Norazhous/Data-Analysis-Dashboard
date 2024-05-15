//Updated to Vue3, removing eventBus implementation, instead nav bar emits up to App which then controls components and passes props to sibling components

<template>

  <nav class="navbar fixed-top navbar-expand-lg navbar-dark background-primary">
    <div class="container-fluid">
        <img src="/practable-icon.png" width="30" height="30" alt="">
      <a class="navbar-brand" href="#">Data Analysis Dashboard: Compression Refrigeration Experiment </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <!-- <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                   Menu
                  </a>
                  <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <li><a class="dropdown-item" href="#" >Component</a></li>
                  </ul>
              </li> -->


              <!-- <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown2" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                   Layout
                  </a>
                  <ul class="dropdown-menu" aria-labelledby="navbarDropdown2">
                    <li><a class="dropdown-item" href="#" @click='toggleLayout(1)'>Single Column</a></li>
                    <li><a class="dropdown-item" href="#" @click='toggleLayout(0.25)'>25%:75%</a></li>
                    <li><a class="dropdown-item" href="#" @click='toggleLayout(0.5)'>50%:50%</a></li>
                    <li><a class="dropdown-item" href="#" @click='toggleLayout(0.75)'>75%:25%</a></li>
                  </ul>
              </li> -->

              <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" id="settingsdropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                   Settings
                  </a>
                  <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDropdown2">
                    <li><a class="dropdown-item" id='toggleconsentbutton' href="#" @click='this.$emit("toggleconsent")'>Change consent</a></li>
                    <!-- <li v-if="getExperiment == 'pendulum'"><a class="dropdown-item" id='changeexperiment' href="#" @click='changeExperiment("spinner")'>Spinner</a></li>
                    <li v-if="getExperiment == 'spinner'"><a class="dropdown-item" id='changeexperiment' href="#" @click='changeExperiment("pendulum")'>Pendulum</a></li> -->
                </ul>
              </li>

              <li class="nav-item dropdown">
                <a class="nav-link" >
                    UUID: {{ getLogUUID }}
                </a> 
              </li>
              
          </ul>

          <div class='d-flex'>
            
            <div v-if="displaySave" class="text-white me-2 mt-2"> {{ dateTime }}</div>
            <button class="btn btn-success me-2" @click="save">Save</button>
            <!-- <button class="btn btn-primary" @click="refresh">Refresh</button> -->
            <!-- <toolbar class='me-5' parentCanvasID="" parentDivID="navbar" parentComponentName="navbar" :showDownload="false" :showOptions="false" :showPopupHelp="true">
                  <template v-slot:popup-help-body id='navbar-popup'>
                    <div class='row'>
                      <div class='col-6'>
                        <h2> Layout </h2>
                        <p> The layout of the UI can be changed using the Layout dropdown menu. This changes the left and right screen column sizes.</p>
                        <p>Components can be swapped by dragging to new positions. Click and drag from near but within the dotted line of the component you want to move. Release 
                          inside the white background of the dotted border that you want to move it to.</p>
                      </div>
                    </div>
                  </template>
            </toolbar> -->

            <ul class="navbar-nav dropstart">
                <li class="nav-item">
                    <clock class='nav-link' />
                  </li>
            </ul>
           
         

          </div>


      </div>
    </div>
  </nav>

</template>

<script>

import Clock from './Clock.vue';
import { mapActions, mapGetters } from 'vuex';

export default {

  name: 'NavigationBar',
  components: {
    Clock
  },
  props:{
      
  },
  emits:[
    'save', 'toggleconsent'
  ],
  data () {
    return {
        displaySave: false,
        dateTime: ''
    }
  },
  computed:{
    ...mapGetters([
        // 'getLogUUID',
        // 'getExperiment'
    ]),

  },
  methods: {
    ...mapActions([
        'requestAll',
        // 'setExperiment'
    ]),
      toggleComponent(component){
          this.$emit('toggle' + component);
      },
      // toggleLayout(ratio){
      //   if(ratio == 0.25)
      //   {
      //     this.$emit('togglelayout', 0.25);
      //   }
      //   else if(ratio == 0.5)
      //   {
      //     this.$emit('togglelayout', 0.5);
      //   }
      //   else if(ratio == 0.75)
      //   {
      //     this.$emit('togglelayout', 0.75);
      //   }
      //   else 
      //   {
      //     this.$emit('togglelayout', 1);
      //   }
      // },
      save(){
        this.$emit('save');
        this.updateDateTime();
        this.displaySave = true;
        this.$store.dispatch('log', {log: "analytics-interaction", type: "save"})
      },
      updateDateTime(){
      let d = new Date();
      let time = d.toLocaleTimeString();
      let date = d.toLocaleDateString();
      this.dateTime = "Saved: " + date + " " + time;
    },
    refresh(){
      this.requestAll();
    },
    // changeExperiment(exp){
    //     this.setExperiment(exp);
    //     this.requestAll();
    // }
  }
}
</script>

<style scoped>


</style>