<template>
    <div>
        <div class="border-dashed row">
            <div class="col-lg-6">
                <h2>Measured Data Input</h2>
                <div class="table-responsive">
                    <table class="table">
                        <thead class="table-light">
                            <tr>
                                <th>Time(min)</th>
                                <th>T1(°C)</th>
                                <th>T2(°C)</th>
                                <th>T3(°C)</th>
                                <th>T4(°C)</th>
                                <th>T5(°C)</th>
                                <!-- <th>P1(bar)</th>
                                <th>P2(bar)</th>
                                <th>P3(bar)</th>
                                <th>F(L/h)</th>
                                <th>E(W)</th> -->
                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>
                                <td><input type="number" name="" class="inputnumber" id="time" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="T1" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="T2" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="T3" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="T4" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="T5" placeholder="0"></td>
                                <!-- <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td> -->
                            </tr>
                        </tbody>
                        <thead class="table-light">
                            <tr>
                                <!-- <th>T1(°C)</th>
                                <th>T2(°C)</th>
                                <th>T3(°C)</th>
                                <th>T4(°C)</th>
                                <th>T5(°C)</th> -->
                                <th>P1(bar)</th>
                                <th>P2(bar)</th>
                                <th>P3(bar)</th>
                                <th>F(L/h)</th>
                                <th>E(W)</th>
                                <th>Ambient Pressure(bar)</th>
                            </tr>
                        </thead>
                        <tbody class="table-group-divider">
                            <tr>
                                <!-- <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td>
                                <td><input type="number" name="" id="inputnumber" placeholder="22"></td> -->
                                <td><input type="number" name="" class="inputnumber" id="P1" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="P2" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="P3" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="F" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="E" placeholder="0"></td>
                                <td><input type="number" name="" class="inputnumber" id="ASP" placeholder="0"></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="row">
                    <div class="col-3">

                    </div>
                    <div class="col-3">
                        <button type="button" class="btn btn-primary" @click="updateChart()">Confirm</button>
                        <!-- <button type="button" class="btn btn-primary">Reset</button> -->
                    </div>
                    <div class="col-3">
                        <button type="button" class="btn btn-primary" @click="reset()">Reset</button>
                    </div>
                    <div class="col-3">
                        <!-- <button @click="GetDataformInput()">test input data</button> -->
                    </div>
                </div>

            </div>
            <div class="col-lg-6">
                <h2>Measured Data Feedback</h2>
                <div>
                    <canvas id="MeasuredDataChart" width="450" height="200"></canvas>
                </div>
            </div>

        </div>

    </div>

</template>

<script>
import Chart from 'chart.js/auto';
import annotationPlugin from 'chartjs-plugin-annotation';
import 'chartjs-plugin-streaming';
// import 'chartjs-adapter-luxon';
// import 'luxon';
import { mapGetters, mapActions } from 'vuex';

export default {
    name: "MeasuredDataFeedback",
    props: {

    },
    data() {
        this.MeasuredDataChart = null
        return {
            DataQualityDataset: [],
            updateFlag: false,
            // inputTime: 0,
        }
    },
    mounted() {
        this.createChart();

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
        ...mapActions([
            'SetMeasuredTime',
            'SetT1',
            'SetT2',
            'SetT3',
            'SetT4',
            'SetT5',
            'SetP1',
            'SetP2',
            'SetP3',
            'SetE',
            'SetF',
            'SetASP',

        ]),

        GetDataformInput(){

            this.SetMeasuredTime(document.getElementById('time').value);
            this.SetT1(document.getElementById('T1').value);
            this.SetT2(document.getElementById('T2').value);
            this.SetT3(document.getElementById('T3').value);
            this.SetT4(document.getElementById('T4').value);
            this.SetT5(document.getElementById('T5').value);
            this.SetP1(document.getElementById('P1').value);
            this.SetP2(document.getElementById('P2').value);
            this.SetP3(document.getElementById('P3').value);
            this.SetE(document.getElementById('E').value);
            this.SetF(document.getElementById('F').value);
            this.SetASP(document.getElementById('ASP').value);
            // console.log(this.GetMeasuredTime, this.GetT1, this.GetT2,this.GetT3,this.GetT4,this.GetT5,this.GetP1,this.GetP2,this.GetP3,this.GetE,this.GetF,this.GetASP);
        },

        //quality curve data 
        QualityDataset() {
            for (let i = 0; i < 70; i++) {
                this.DataQualityDataset.push({
                    x: i,
                    y: 1 - Math.exp(-i * 0.1)
                })
            };

        },

        //init chart
        createChart() {
            Chart.register(annotationPlugin);
            // Initialize Chart.js
            var ctx = document.getElementById('MeasuredDataChart').getContext('2d');
            this.MeasuredDataChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: [], // Fixed x-axis labels
                    datasets: [{
                        label: 'Data Quality Curve',
                        backgroundColor: 'rgb(255, 0, 0)',
                        borderColor: 'rgb(255, 0, 0)',
                        borderWidth: 1,
                        data: [],  // Initialize with empty data
                        pointRadius: 0,
                        // hidden: () => this.updateAction(),
                    },

                    {
                        label: 'Your Data',
                        backgroundColor: 'rgb(0, 0, 255)',
                        borderColor: 'rgb(0, 0, 255)',
                        borderWidth: 1,
                        data: [],
                        pointRadius: 8,
                        pointStyle: 'rectRot',
                    },],
                },
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            type: 'linear', // Fixed x-axis scale
                            position: 'bottom', // Position x-axis at the bottom
                            ticks: {
                                stepSize: 5, // Step size for x-axis
                                min: 0,      // Minimum value for x-axis
                                max: 500,      // Maximum value for x-axis
                            },
                            title: {
                                display: true,
                                text: 'Time/min'
                            }
                        },
                        y: {
                            ticks: {
                                display: false
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Value',
                            },
                            title: {
                                display: true,
                                text: 'Data Quality'
                            }
                        }
                    },
                    plugins: {
                        annotation: {
                            annotations: {
                                box1: {
                                    type: 'box',
                                    xMin: 20,
                                    xMax: 45,
                                    yMin: 0,
                                    yMax: 1.6,
                                    backgroundColor: 'rgba(255,165,0, 0.25)',
                                    borderColor: 'rgba(255,165,0, 0.25)',
                                    display: () => this.updateAction(),
                                    drawTime: 'afterDraw',
                                },
                                label1: {
                                    display: () => this.updateAction(),
                                    type: 'label',
                                    xValue: 33,
                                    yValue: 0.3,
                                    backgroundColor: 'rgba(245,245,245)',
                                    content: ['Best Range'],
                                    font: {
                                        size: 18
                                    }
                                }
                            }
                        }
                    },

                },
            });
        },

        //update function for display the element in the chart
        updateAction() {
            return this.updateFlag;
        },

        // update the elements and the curve in the chart
        updateChart() {
            this.GetDataformInput();
            // this.inputTime = document.getElementById('time').value;
            if (this.MeasuredDataChart.data.datasets[0].data.length == 0 && this.GetMeasuredTime != '' && this.DataQualityDataset.length == 0) {
                //update the quality line in the chart and show the best range annotation
                this.updateFlag = true;
                this.QualityDataset();
                this.MeasuredDataChart.data.datasets[0].data = this.DataQualityDataset;

                //update the data input
                // let inputTime = document.getElementById('time').value;
                let qualityCalculation = 1 - Math.exp(-this.GetMeasuredTime * 0.1);
                this.MeasuredDataChart.data.datasets[1].data.push({
                    x: this.GetMeasuredTime,
                    y: qualityCalculation,
                }),
                    this.MeasuredDataChart.update();

            } else if (this.GetMeasuredTime == '') {
                alert("Please input measured data!")

            }
            else {
                this.updateFlag = true;
                this.MeasuredDataChart.data.datasets[0].data = this.DataQualityDataset;
                //update the data input 
                this.GetMeasuredTime = document.getElementById('time').value;
                let qualityCalculation = 1 - Math.exp(-this.GetMeasuredTime * 0.1);
                this.MeasuredDataChart.data.datasets[1].data = [];
                this.MeasuredDataChart.data.datasets[1].data.push({
                    x: this.GetMeasuredTime,
                    y: qualityCalculation,
                }),
                    this.MeasuredDataChart.update();
            }

        },

        //clear and reset the data in the input form and chart
        reset() {
            this.updateFlag = false;
            this.MeasuredDataChart.data.datasets[0].data = [];
            this.MeasuredDataChart.data.datasets[1].data = [];
            this.MeasuredDataChart.update();
        },


    },


};
</script>

<style>
.inputnumber {
    width: 70px;
}
</style>