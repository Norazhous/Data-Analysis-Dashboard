<template>
    <div class="border-dashed">
        <!-- <div class="row">
            <div class="col-lg-6"> -->
        <h2> Calculation Results (Student) </h2>
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
                        <td><input type="number" name="" class="inputnumber" id="H1" placeholder="0" value="400"></td>
                        <td><input type="number" name="" class="inputnumber" id="H2" placeholder="0" value="400"></td>
                        <td><input type="number" name="" class="inputnumber" id="H3" placeholder="0" value="200"></td>
                        <td><input type="number" name="" class="inputnumber" id="H4" placeholder="0" value="200"></td>
                        <td><input type="number" name="" class="inputnumber" id="H5" placeholder="0" value="400"></td>
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
                        <!-- <th>Compressor work</th>
                            <th>Coefficient of performance </th>
                            <th>Compressor compression ratio</th> -->
                    </tr>
                </thead>
                <tbody class="table-group-divider">
                    <tr>

                        <td><input type="number" name="" class="inputnumber" id="m" placeholder="0" value="0.01"></td>
                        <td><input type="number" name="" class="inputnumber" id="QL" placeholder="0" value="60"></td>
                        <td><input type="number" name="" class="inputnumber" id="QH" placeholder="0" value="50"></td>
                        <!-- <td><input type="number" name="" class="inputnumber" id="F" placeholder="22"></td>
                            <td><input type="number" name="" class="inputnumber" id="E" placeholder="22"></td>
                            <td><input type="number" name="" class="inputnumber" id="E" placeholder="22"></td> -->

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
                        <td><input type="number" name="" class="inputnumber" id="W" placeholder="0" value="250"></td>
                        <td><input type="number" name="" class="inputnumber" id="COP" placeholder="0" value="5"></td>
                        <td><input type="number" name="" class="inputnumber" id="n" placeholder="0" value="5"></td>

                    </tr>
                </tbody>
            </table>

        </div>
        <div class="row">
            <div class="col-3">

            </div>
            <div class="col-3">
                <button class="btn btn-primary" @click="GetDataformInput">Confirm</button>
            </div>
            <div class="col-3">
                <button class="btn btn-primary" @click="reset">Reset</button>
            </div>
        </div>
        <div class="col-3">

        </div>
    </div>


    <!-- </div>
    </div> -->


</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    name: "TableStudentCalculation",
    props: {

    },
    data() {
        return {

        };
    },
    mounted() {


    },
    computed: {
        ...mapGetters([
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
            'SetH1',
            'SetH2',
            'SetH3',
            'SetH4',
            'SetH5',
            'Setm',
            'SetQL',
            'SetQH',
            'SetW',
            'SetCOP',
            'Setn',
            'SetCalcuDataConfirmed',
        ]),

        GetDataformInput() {
            this.SetH1(document.getElementById('H1').value);
            this.SetH2(document.getElementById('H2').value);
            this.SetH3(document.getElementById('H3').value);
            this.SetH4(document.getElementById('H4').value);
            this.SetH5(document.getElementById('H5').value);
            this.Setm(document.getElementById('m').value);
            this.SetQL(document.getElementById('QL').value);
            this.SetQH(document.getElementById('QH').value);
            this.SetW(document.getElementById('W').value);
            this.SetCOP(document.getElementById('COP').value);
            this.Setn(document.getElementById('n').value);
            this.SetCalcuDataConfirmed(1);
            // console.log(this.GetH1, this.GetH2,this.GetH3,this.GetH4,this.GetH5,
            // this.Getm,this.GetQL,this.GetQH,this.GetW,this.GetCOP,this.Getn);
        },

        ClearformInput() {
            document.getElementById('H1').value = 0;
            document.getElementById('H2').value = 0;
            document.getElementById('H3').value = 0;
            document.getElementById('H4').value = 0;
            document.getElementById('H5').value = 0;
            document.getElementById('m').value = 0;
            document.getElementById('QL').value = 0;
            document.getElementById('QH').value = 0;
            document.getElementById('W').value = 0;
            document.getElementById('COP').value = 0;
            document.getElementById('n').value = 0;
        },

        //clear and reset the data in the input form and chart
        reset() {
            this.ClearformInput();
            this.GetDataformInput();
            this.SetCalcuDataConfirmed(0);

        },


    },

};
</script>

<style></style>