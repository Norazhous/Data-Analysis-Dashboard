<template>
    <div class="border-dashed">
        <div class="row">
            <div class="col-lg-6">
                <h2> p-h Chart for Enthalpy Value (Student)</h2>
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
                    <canvas ref="canvas" @mousedown="startDrawing" @mouseup="endDrawing" @mousemove="drawLine"></canvas>
                </div>
                <div class="row" id="buttongroup">
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
            canvas: null,
            ctx: null,
            rect: null,
            straightLine: false,
            lines: [],
            mouseX: 0,
            mouseY: 0,
            pencilPath: [],
            line: [],

        };
    },
    mounted() {

        this.setupCanvas();
        // window.addEventListener('resize', this.setupCanvas);
    },
    // beforeDestroy() {
    //     window.removeEventListener('resize', this.setupCanvas); // Clean up the event listener
    // },
    methods: {
        setupCanvas() {
            this.canvas = this.$refs.canvas;
            this.ctx = this.$refs.canvas.getContext('2d');
            // const canvas = this.$refs.canvas;
            // const parent = document.getElementById('parent');
            // canvas.width = parent.offsetWidth;
            // canvas.height = parent.offsetHeight;
            this.canvas.width = this.canvas.offsetWidth;
            this.canvas.height = this.canvas.offsetHeight;
            this.rect = this.$refs.canvas.getBoundingClientRect();
        },

        // drawing lines function
        startDrawing(e) {
            this.drawing = true;
            this.startX = e.clientX - this.rect.left;
            this.startY = e.clientY - this.rect.top;
            this.drawLine(e);


        },
        endDrawing() {
            this.drawing = false;
            // this.$refs.canvas.getContext('2d').beginPath();
            if (this.straightLine == false) {
                //console.log(this.pencilPath);
                var line = this.line;
                this.pencilPath.push({ line });
                // console.log(this.pencilPath);
                this.line = [];
                this.ctx.beginPath();

            } else {
                this.lines.push({
                    startX: this.startX,
                    startY: this.startY,
                    endX: this.mouseX,
                    endY: this.mouseY
                });
                // this.clearAndRedraw();
                this.ctx.beginPath();
            }

        },
        drawLine(e) {
            if (!this.drawing) return;
            if (this.drawing) {
                this.mouseX = e.clientX - this.rect.left;
                this.mouseY = e.clientY - this.rect.top;

                if (this.straightLine == false) {

                    this.ctx.lineWidth = 2;
                    this.ctx.strokeStyle = '#FFAC1C';
                    this.ctx.lineTo(this.mouseX, this.mouseY);
                    this.ctx.stroke();

                    this.ctx.beginPath();
                    this.ctx.moveTo(this.mouseX, this.mouseY);

                    var x = this.mouseX;
                    var y = this.mouseY;

                    this.line.push({ x, y });

                } else {

                    this.ctx.lineWidth = 2;

                    this.clearAndRedraw();

                    this.ctx.strokeStyle = "darkred";
                    this.ctx.lineWidth = 3;
                    this.ctx.beginPath();
                    this.ctx.moveTo(this.startX, this.startY);
                    this.ctx.lineTo(this.mouseX, this.mouseY);
                    this.ctx.stroke();

                }

            }

        },
        clearLine() {
            this.drawing = false;
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.lines = [];
            this.pencilPath = [];
            console.log("clear")
        },
        straightLineDrawing() {
            this.straightLine = true;

        },
        //Clear and redraw the canvas
        clearAndRedraw() {
            this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
            this.lines.forEach(line => {
                this.ctx.beginPath();
                // console.log(line);
                this.ctx.moveTo(line.startX, line.startY);
                this.ctx.lineTo(line.endX, line.endY);
                this.ctx.stroke();
            });
            this.pencilPath.forEach(line => {

                for (let i = 1; i < line.line.length; i++) {
                    this.ctx.beginPath();
                    this.ctx.lineWidth = 2;
                    this.ctx.strokeStyle = '#FFAC1C';
                    this.ctx.moveTo(line.line[i - 1].x, line.line[i - 1].y);
                    this.ctx.lineTo(line.line[i].x, line.line[i].y);
                    // console.log(line.line);
                    // console.log(i);
                    // console.log("i"+line.line[i].x);
                    // console.log("i+1"+line.line[i+1].x);
                    // console.log(this.pencilPath.line[i].x, this.pencilPath.line[i].y);
                    this.ctx.stroke();
                };
            });
            this.ctx.beginPath();


        },


        pencil() {
            this.straightLine = false;
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
    height: 100%;
    position: absolute;

}
</style>