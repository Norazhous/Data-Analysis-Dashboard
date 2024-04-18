<template>
    <div class="border-dashed">
        <div class="row">
            <div class="col-lg-6">
                <h2> p-h Chart for Enthalpy Value (Student)</h2>
               
                <div id="parent" class="image-container">

                    <!-- <img src="../assets/R134_p_h_diagram.svg" alt="Background" @load="adjustCanvasSize"> -->
                    <!-- <img src="/images/R134_p_h_diagram.svg" alt="Background"> -->
                    <canvas ref="canvas" @mousedown="startDrawing" @mouseup="endDrawing" @mousemove="drawLine"
                        @mouseout="endDrawing"></canvas>
                </div>
                <div class="row">
                    <div class="col-lg-3">
                        <button type="button" class="col-12 btn btn-primary" @click="clearLine">Plotting line </button>
                    </div>
                    <div class="col-lg-3">
                        <button type="button" class="col-12 btn btn-primary" @click="clearLine">Straight line </button>
                    </div>
                    <div class="col-lg-3">
                        <button type="button" class="col-12 btn btn-primary" @click="clearLine">Clear</button>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
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
                                <td><input type="number" name="" class="inputnumber" id="H1" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="H2" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="H3" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="H4" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="H5" placeholder="22"></td>
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

                                <td><input type="number" name="" class="inputnumber" id="m" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="QL" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="QH" placeholder="22"></td>
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
                                <td><input type="number" name="" class="inputnumber" id="W" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="COP" placeholder="22"></td>
                                <td><input type="number" name="" class="inputnumber" id="n" placeholder="22"></td>

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
    name: "CanvasDrawing",
    props: {

    },
    data() {
        return {
            drawing: false,
            startX: 0,
            startY: 0,
        };
    },
    mounted() {
        // adjust the size of the canvas
        // this.$nextTick(() => {
        //     const canvas = this.$refs.canvas;
        //     const parent = document.getElementById('parent')
        //     // canvas.width = window.innerWidth;
        //     // canvas.height = window.innerHeight;
        //     // canvas.style.width = parent.height;
        //     // canvas.style.height = parent.height;
        //     // canvas.width = parent.offsetWidth;
        //     // canvas.height = parent.offsetHeight;
        //     // canvas.style.width = '100%';
        //     // canvas.style.height = '100%';
        //     canvas.width = canvas.offsetWidth;
        //     canvas.height = canvas.offsetHeight;
        // });
        this.setupCanvas();
        // window.addEventListener('resize', this.setupCanvas);
    },
    // beforeDestroy() {
    //     window.removeEventListener('resize', this.setupCanvas); // Clean up the event listener
    // },
    methods: {
        setupCanvas() {
            const canvas = this.$refs.canvas;
            // const parent = document.getElementById('parent');
            // canvas.width = parent.offsetWidth;
            // canvas.height = parent.offsetHeight;
            canvas.width = canvas.offsetWidth;
            canvas.height = canvas.offsetHeight;
        },

        // drawing lines function
        startDrawing(e) {
            this.drawing = true;
            const rect = this.$refs.canvas.getBoundingClientRect();
            console.log(rect);
            // e.clientX = rect.left;
            // e.clientY = rect.top;
            this.startX = e.clientX - rect.left;
            this.startY = e.clientY - rect.top;
            this.drawLine(e);
            console.log(e);
        },
        endDrawing() {
            this.drawing = false;
            this.$refs.canvas.getContext('2d').beginPath();
        },
        drawLine(e) {
            if (!this.drawing) return;
            const ctx = this.$refs.canvas.getContext('2d');
            const rect = this.$refs.canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            ctx.lineWidth = 2;
            ctx.strokeStyle = '#FFAC1C';
            ctx.lineTo(x, y);
            ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(x, y);
        },
        clearLine() {
            this.drawing = false;
            const canvas = this.$refs.canvas;
            const ctx = this.$refs.canvas.getContext('2d');
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            console.log("clear")
        }
    },
    //https://stackoverflow.com/questions/49885020/drawing-a-straight-line-using-mouse-events-on-canvas-in-javascript
};
</script>

<style>
.image-container {
    display: inline-block;
    width: 100%;
    height: 500px;
    position: relative;

}

.image-container canvas {
    background: url(../assets/Chart-p-h-R134a-1.png);
    background-size: 100% 100%;
    top: 0;
    left: 0;
    width: 100%;
    height: 95%;
    position: absolute;

}
</style>