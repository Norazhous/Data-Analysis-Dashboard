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
                                <td><input type="number" name="" class="inputnumber" id="time" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="T1" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="T2" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="T3" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="T4" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="T5" placeholder="22"></td>
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
                                <td><input type="number" name="" class="inputnumber" id="P1" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="P2" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="P3" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="F" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="E" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="ASP" placeholder="22"></td>
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

export default {
    name: "MeasuredDataFeedback",
    props: {

    },
    data() {
        this.MeasuredDataChart = null
        return {
            DataQualityDataset: [],
            updateFlag: false,
            inputTime: 0, 
        }
    },
    mounted() {
        this.createChart();

    },
    methods: {

        QualityDataset() {
            for (let i = 0; i < 70; i++) {
                this.DataQualityDataset.push({
                    x: i,
                    y: 1 - Math.exp(-i * 0.1)
                })
            };

        },


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

        //update function for dispaly
        updateAction() {
            return this.updateFlag;
        },


        updateChart() {
            this.inputTime = document.getElementById('time').value;
            if (this.MeasuredDataChart.data.datasets[0].data.length == 0 && this.inputTime != ''&& this.DataQualityDataset.length ==0) {
                //update the quality line in the chart and show the best range annotation
                this.updateFlag = true;
                this.QualityDataset();
                this.MeasuredDataChart.data.datasets[0].data = this.DataQualityDataset;

                //update the data input
                // let inputTime = document.getElementById('time').value;
                let qualityCalculation = 1 - Math.exp(-this.inputTime * 0.1);
                this.MeasuredDataChart.data.datasets[1].data.push({
                    x: this.inputTime,
                    y: qualityCalculation,
                }),
                this.MeasuredDataChart.update();

            } else if (this.inputTime == '') {
                alert("Please input measured data!")

            }
            else {
                this.updateFlag = true;
                this.MeasuredDataChart.data.datasets[0].data = this.DataQualityDataset;
                //update the data input 
                this.inputTime = document.getElementById('time').value;
                let qualityCalculation = 1 - Math.exp(-this.inputTime * 0.1);
                this.MeasuredDataChart.data.datasets[1].data = [];
                this.MeasuredDataChart.data.datasets[1].data.push({
                    x: this.inputTime,
                    y: qualityCalculation,
                }),
                this.MeasuredDataChart.update();
            }

        },

        //reset the data in the input form and feedback chart
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