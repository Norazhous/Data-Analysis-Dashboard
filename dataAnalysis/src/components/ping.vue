<template>
  <div>
    <p>{{ msg }}</p>
    <input id="postTest" type="number">
    <input id="postTest1" type="number">
    <button @click="test"> add</button>
  </div>
</template>

<script>
import axios from 'axios';


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
      this.H3 = document.getElementById('postTest').value;
      this.H4 = document.getElementById('postTest1').value;
      if (this.H3 != ''&&this.H4 != '') {
        const payload = {
          'H3': Number(this.H3),
          'H4': Number(this.H4),
        };
        this.postMessage(payload);
        console.log(payload);
      }
     
    }
  }
};
</script>