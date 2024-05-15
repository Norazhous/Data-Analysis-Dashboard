<template>
  <div>
    <p>{{ msg }}</p>
    <button @click="test"> add</button>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';

export default {
  name: 'test',
  data() {
    return {
      msg: 'Hello!',
      H3: 0,
      H4: 0,
    };
  },
  created() {
    this.getMessage();
  },
  computed: {
        ...mapGetters([
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
        ])
    },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/test';
      axios.get(path)
        .then((res) => {
          this.msg = res.data.Parameters;
        })
        .catch((error) => {
          console.log(error);
        })
    },

    postMessage(payload) {
      const path = 'http://127.0.0.1:5000/test';
      axios.post(path, payload)
        .then(() => {
          this.getMessage();
        })
        .catch((error) => {

          console.log(error);
          this.getMessage();
        });
    },


    test() {
     
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
        };
        this.postMessage(payload);
        console.log(payload);
      // }
     
    }
  }
};
</script>