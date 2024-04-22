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
                    <img src="../assets/R134_p_h_diagram_with_cycle.svg" alt="" style="width: 550px; height: 400px;">
                </div>
               

            </div>
            <div class="col-lg-6">
                <h2> Calculation Results (system) </h2>
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
                                <td>22</td>
                                <td>22</td>
                                <td>22</td>
                                <td>22</td>
                                <td>22</td>
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

                                <td>22</td>
                                <td>22</td>
                                <td>22</td>
                           
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
                                <td>22</td>
                                <td>22</td>
                                <td>22</td>

                            </tr>
                        </tbody>
                    </table>
                    <table class="table">
                        <thead class="table-light">
                            <tr>
                                <th colspan="5">Saturated vapor or liquid value</th>
                            </tr>
                            <tr>

                                <th>Saturated Temperature under P1</th>
                                <th>Saturated Temperature under P2</th>
                                <th>Saturated Pressure under T3</th>
                                <th>Saturated Pressure under T5</th>                               
                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>
                                <td>22</td>
                                <td>22</td>
                                <td>22</td>
                                <td>22</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
export default {
    name: "DataFetch",
    props: {

    },
    data() {
        return {
       

        };
    },
    mounted() {

    
    },
    methods: {
       
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