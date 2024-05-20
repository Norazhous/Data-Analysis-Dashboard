<template>
    <div class="border-dashed">
        <div class="row">
            <div class="col-lg-6">
                <h2> p-h Chart for Enthalpy Value (system)</h2>
                <!-- <div class="row" id="buttongroup">
                        <div class="col-lg-3">
                            <button type="button" class="col-12 btn btn-primary" @click="pencil()">Pencil
                            </button>
                        </div>
                        <div class="col-lg-3">
                            <button type="button" class="col-12 btn btn-primary" @click="straightLineDrawing()">Straight
                                line </button>
                        </div>
                        <div class="col-lg-3">
                            <button type="button" class="col-12 btn btn-primary" @click="clearLine()">Clear</button>
                        </div>
                    </div> -->
                <div id="parent" class="image-container">
                    <!-- <img src="../assets/R134_p_h_diagram.svg" alt="Background" @load="adjustCanvasSize"> -->
                    <!-- <img src="/images/R134_p_h_diagram.svg" alt="Background"> -->
                    <!-- <img src="../assets/R134_p_h_diagram_with_cycle.svg" alt="" style="width: 550px; height: 400px;"> -->
                    <img :src="GetImgData" alt="" style="width: 550px; height: 400px;">
                </div>


            </div>
            <div class="col-lg-6">
                <h2> Calculation compare (system) </h2>
                <div class="table-responsive">
                    <table class="table">
                        <thead class="table-light">
                            <tr>
                                <th colspan="5">Enthalpy Value</th>
                            </tr>
                            <tr>

                                <th>H1(KJ/Kg)</th>
                                <th>H2(KJ/Kg)</th>
                                <th>H3(KJ/Kg)</th>
                                <th>H4(KJ/Kg)</th>
                                <th>H5(KJ/Kg)</th>

                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>
                                <td>{{ this.GetH1_Dev }}</td>
                                <td>{{ this.GetH2_Dev }}</td>
                                <td>{{ this.GetH3_Dev }}</td>
                                <td>{{ this.GetH4_Dev }}</td>
                                <td>{{ this.GetH5_Dev }}</td>
                            </tr>
                        </tbody>
                    </table>
                    <table class="table">
                        <thead class="table-light">
                            <tr>
                                <th colspan="3">Parameters Calculation</th>
                            </tr>
                            <tr>
                                <th>Mass flowrate m(Kg/s)</th>
                                <th>Refrigeration capacity QL(KW)</th>
                                <th>Condensation capacity QH(KW)</th>

                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>

                                <td>{{ this.Getm_Dev }}</td>
                                <td>{{ this.GetQL_Dev }}</td>
                                <td>{{ this.GetQH_Dev }}</td>

                            </tr>
                        </tbody>
                        <thead class="table-light">
                            <tr>
                                <th>Compressor work W(KW)</th>
                                <th>Coefficient of performance COP</th>
                                <th>Compressor compression ratio η</th>
                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>
                                <td>{{ this.GetW_Dev }}</td>
                                <td>{{ this.GetCOP_Dev }}</td>
                                <td>{{ this.Getn_Dev }}</td>

                            </tr>
                        </tbody>
                    </table>
                    <table class="table">
                        <thead class="table-light">
                            <tr>
                                <th colspan="5">Saturated vapor or liquid value</th>
                            </tr>
                            <tr>

                                <th>Saturated Temperature(°C) under P1</th>
                                <th>Saturated Temperature(°C) under P2</th>
                                <th>Saturated Pressure(bar) under T3</th>
                                <th>Saturated Pressure(bar) under T5</th>
                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>
                                <td>{{this.GetSaturT_P1}}</td>
                                <td>{{ this.GetSaturT_P2 }}</td>
                                <td>{{ this.GetSaturP_T3/100000 }}</td>
                                <td>{{ this.GetSaturP_T5/100000 }}</td>
                            </tr>
                        </tbody>
                    </table>
                    <!-- <button @click="test">{{ GetImgData }}</button> -->
                </div>
            </div>
        </div>
    </div>


</template>

<script>
import { mapGetters } from 'vuex';

export default {
    name: "DataCompare",
    props: {

    },
    data() {
        return {
            // imgData:null,

        };
    },
    mounted() {


    },
    computed: {
        ...mapGetters([
            //get deviation data from the store 
            'GetH1_Dev',
            'GetH2_Dev',
            'GetH3_Dev',
            'GetH4_Dev',
            'GetH5_Dev',
            'Getm_Dev',
            'GetQL_Dev',
            'GetQH_Dev',
            'GetW_Dev',
            'GetCOP_Dev',
            'Getn_Dev',
            'GetSaturT_P1',
            'GetSaturT_P2',
            'GetSaturP_T3',
            'GetSaturP_T5',
            //get img_data from the store
            'Getimg_data'
        ]),

        GetImgData(){
            if(this.Getimg_data != null){
                return "data:image/png;base64," + this.Getimg_data
            }
            else{
                return "public/practable-icon.png"
            }
        },


    },
    methods: {
        test(){
            console.log(this.Getimg_data);
            console.log(this.imgData);
        },

        // GetImgData(){
        //     if(this.Getimg_data != null){
        //         return "data:image/png;base64," + this.Getimg_data
        //     }
        //     else{
        //         return "dataAnalysis/public/test.svg"
        //     }
        // }

       
    },

};
</script>

<style>
.image-container {
    display: inline-block;
    width: 100%;
    height: 400px;
    position: relative;

}
</style>