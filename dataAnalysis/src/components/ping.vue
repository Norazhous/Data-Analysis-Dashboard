<template>
  <div class="border-dashed">
    <!-- <p>{{ msg }}</p> -->
    <h2> Submit data to the server and get feedback </h2>
    <p>(This section will only be displayed after students agree the consent)</p>
    <div class="row">
      <div class="col-lg-3">
       
      </div>
      <div class="col-lg-3">
        <button class="btn btn-primary" @click="SubmitMeasuredData"> Submit Measured Data</button>
      </div>
      <div class="col-lg-3">
        <button class="btn btn-primary" @click="SubmitCalculationData"> Submit Calculation Data</button>
      </div>
      <div class="col-lg-3">
       
      </div>
    </div>


  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'enthapy',
  data() {
    return {
      msg: 'Hello!',
      H3: 0,
      H4: 0,
    };
  },
  created() {
    // this.getMessage();
  },
  computed: {
    ...mapGetters([
      //get measured data from store
      'GetMeasuredTime',
      'GetT1',
      'GetT2',
      'GetT3',
      'GetT4',
      'GetT5',
      'GetP1',
      'GetP2',
      'GetP3',
      'GetE',
      'GetF',
      'GetASP',
      //get student calculation data from store
      'GetH1',
      'GetH2',
      'GetH3',
      'GetH4',
      'GetH5',
      'Getm',
      'GetQL',
      'GetQH',
      'GetW',
      'GetCOP',
      'Getn',

    ])
  },
  methods: {
    ...mapActions([
      //get deviation data and set them in the store 
      'SetH1_Dev',
      'SetH2_Dev',
      'SetH3_Dev',
      'SetH4_Dev',
      'SetH5_Dev',
      'Setm_Dev',
      'SetQL_Dev',
      'SetQH_Dev',
      'SetW_Dev',
      'SetCOP_Dev',
      'Setn_Dev',
      //get saturated data and set them in the store
      'SetSaturT_P1',
      'SetSaturT_P2',
      'SetSaturP_T3',
      'SetSaturP_T5',
      //get img_data from server and set it in the store
      'Setimg_data'
    ]),

    getMessage() {
      const path = 'http://127.0.0.1:5000/enthapy';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          // this.SetH1_DEV(res.data.Parameters_DeviationCaculation.H1_Dev);
          // this.SetH2_DEV(res.data.Parameters_DeviationCaculation.H2_Dev);
          // this.SetH3_DEV(res.data.Parameters_DeviationCaculation.H3_Dev);
          // this.SetH4_DEV(res.data.Parameters_DeviationCaculation.H4_Dev);
          // this.SetH5_DEV(res.data.Parameters_DeviationCaculation.H5_Dev);
          // this.Setm_DEV(res.data.Parameters_DeviationCaculation.m_Dev);
          // this.SetQL_DEV(res.data.Parameters_DeviationCaculation.QL_Dev);
          // this.SetQH_DEV(res.data.Parameters_DeviationCaculation.QH_Dev);
          // this.SetW_DEV(res.data.Parameters_DeviationCaculation.W_Dev);
          // this.SetCOP_DEV(res.data.Parameters_DeviationCaculation.COP_Dev);
          // this.Setn_DEV(res.data.Parameters_DeviationCaculation.n_Dev);
          this.$store.dispatch('SetH1_Dev', res.data.Parameters_DeviationCaculation.H1_Dev);
          this.$store.dispatch('SetH2_Dev', res.data.Parameters_DeviationCaculation.H2_Dev);
          this.$store.dispatch('SetH3_Dev', res.data.Parameters_DeviationCaculation.H3_Dev);
          this.$store.dispatch('SetH4_Dev', res.data.Parameters_DeviationCaculation.H4_Dev);
          this.$store.dispatch('SetH5_Dev', res.data.Parameters_DeviationCaculation.H5_Dev);
          this.$store.dispatch('Setm_Dev', res.data.Parameters_DeviationCaculation.m_Dev);
          this.$store.dispatch('SetQL_Dev', res.data.Parameters_DeviationCaculation.QL_Dev);
          this.$store.dispatch('SetQH_Dev', res.data.Parameters_DeviationCaculation.QH_Dev);
          this.$store.dispatch('SetW_Dev', res.data.Parameters_DeviationCaculation.W_Dev);
          this.$store.dispatch('SetCOP_Dev', res.data.Parameters_DeviationCaculation.COP_Dev);
          this.$store.dispatch('Setn_Dev', res.data.Parameters_DeviationCaculation.n_Dev);
          this.$store.dispatch('SetSaturT_P1', res.data.Parameters_SaturatedValue.SaturT_P1);
          this.$store.dispatch('SetSaturT_P2', res.data.Parameters_SaturatedValue.SaturT_P2);
          this.$store.dispatch('SetSaturP_T3', res.data.Parameters_SaturatedValue.SaturP_T3);
          this.$store.dispatch('SetSaturP_T5', res.data.Parameters_SaturatedValue.SaturP_T5);
          this.$store.dispatch('Setimg_data', res.data.img_data);
          console.log(this.msg);
        })
        .catch((error) => {
          console.log(error);
        })
    },

    postMessage(payload) {
      const path = 'http://127.0.0.1:5000/enthapy';
      axios.post(path, payload)
        .then(() => {
          this.getMessage();
        })
        .catch((error) => {

          console.log(error);
          // alert(error.response.data);
          // this.getMessage();
        });
    },


    SubmitMeasuredData() {
      // if (this.H3 != ''&&this.H4 != '') {
      const payload = {
        'MeasuredTime': Number(this.GetMeasuredTime),
        'T1': Number(this.GetT1),
        'T2': Number(this.GetT2),
        'T3': Number(this.GetT3),
        'T4': Number(this.GetT4),
        'T5': Number(this.GetT5),
        'P1': Number(this.GetP1),
        'P2': Number(this.GetP2),
        'P3': Number(this.GetP3),
        'E': Number(this.GetE),
        'F': Number(this.GetF),
        'ASP': Number(this.GetASP),
        'dataType': 'Measured',
      };
      this.postMessage(payload);
      console.log(payload);
      // }
    },

    SubmitCalculationData() {
      const payload = {
        'H1': Number(this.GetH1),
        'H2': Number(this.GetH2),
        'H3': Number(this.GetH3),
        'H4': Number(this.GetH4),
        'H5': Number(this.GetH5),
        'm': Number(this.Getm),
        'QL': Number(this.GetQL),
        'QH': Number(this.GetQH),
        'W': Number(this.GetW),
        'COP': Number(this.GetCOP),
        'n': Number(this.Getn),
        'dataType': 'Calculation',
      };
      this.postMessage(payload);
      console.log(payload);
    }
  }
};
</script>