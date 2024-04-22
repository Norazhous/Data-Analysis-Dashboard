<template>
    <div id='canvasPlot' class="border-dashed">
        <!-- <div class="row">
            <div class="col-lg-6"> -->
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
        <span style="color: red;">{{ message }}</span>
        <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
            <button type="button" class="btn btn-primary" @click="fullScreen()">Full Screen</button>
            <button type="button" class="btn btn-primary" @click="setupCanvas()">Load Canvas</button>
            <!-- <button type="button" class="btn btn-primary" @click="pencil()">Pencil</button>
            <button type="button" class="btn btn-primary" @click="straightLineDrawing()">Straight line </button> -->
            <button type="button" class="btn btn-primary" @click="clearLine()">Clear Canvas</button>
            <div class="btn-group" role="group">
                <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown"
                    aria-expanded="false">
                    Plot Line
                </button>
                <ul class="dropdown-menu">
                    <li><input type="button" class="dropdown-item" @click="pencil()" value="Pencil" /></li>
                    <li><input type="button" class="dropdown-item" @click="straightLineDrawing()"
                            value="Straight line" /></li>
                </ul>
            </div>
            <!-- <button type="button" class="btn btn-primary" @click="download()">Download</button> -->
            <!-- <div class="col-lg-2">
                <button type="button" class="btn btn-primary" @click="fullScreen()">Full Screen</button>
            </div>
            <div class="col-lg-2">
                <button type="button" class="btn btn-primary" @click="setupCanvas()">Load Canvas</button>
            </div>

            <div class="col-lg-2">
                <button type="button" class="btn btn-primary" @click="pencil()">Pencil
                </button>
            </div>
            <div class="col-lg-2">
                <button type="button" class="btn btn-primary" @click="straightLineDrawing()">Straight line </button>
            </div>
            <div class="col-lg-2">
                <button type="button" class="btn btn-primary" @click="clearLine()">Clear</button>
            </div> -->

        </div>

    </div>

    <!-- </div>
    </div> -->


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
            loaded: false,
            message: '',

        };
    },
    mounted() {

        // this.setupCanvas();
        // window.addEventListener('resize', this.setupCanvas);
    },
    // beforeDestroy() {
    //     window.removeEventListener('resize', this.setupCanvas); // Clean up the event listener
    // },
    methods: {
        // download() {    
        //     this.canvas = this.$refs.canvas;
        //     this.ctx = this.$refs.canvas.getContext('2d');
        //     this.ctx.globalCompositeOperation = "destination-over";
        //     const parent = document.getElementById('parent');

        //     var background = new Image();
        //     background.src = 'http://localhost:5173/src/assets/Chart-p-h-R134a-1.png';  // Corrected the src path.
        //     console.log('222');
        //     background.onload = () => {
                
        //         // this.background.width = '100%';
        //         // this.background.height = '100%';
        //         this.ctx.drawImage(background, 0, 0,300,300 * background.height / background.width);
        //         console.log('111');
        //         // Ensure the image is drawn before converting canvas to data URL.
        //         var image = this.canvas.toDataURL("image/jpeg");  // Corrected the MIME type.
        //         var link = document.createElement('a');
        //         link.download = "my-image.jpg";
        //         link.href = image;
        //         // document.body.appendChild(link);  // Append the link to the body.
        //         link.click();  // Trigger the download.
        //         // document.body.removeChild(link);  // Clean up: remove the link after clicking.
        //         //https://stackoverflow.com/questions/10841532/canvas-drawimage-scaling
        //     };
        //     background.onerror = function () {
        //         console.error("The image could not be loaded.");
        //     };

        // },

        focusToCanvas() {
            // window.location.hash = '#parent';
            this.$refs.canvas.scrollIntoView();
        },

        fullScreen() {
            var el = document.getElementById('canvasPlot');

            if (el.webkitRequestFullScreen) {
                el.webkitRequestFullScreen();
            }
            else {
                el.mozRequestFullScreen();
            };


        },

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
            this.lines = [];
            this.pencilPath = [];
            this.drawing = false;
            this.loaded = true;
            this.message = '';

        },

        // drawing lines function
        startDrawing(e) {
            if (this.loaded == true) {
                this.drawing = true;
                this.startX = e.clientX - this.rect.left;
                this.startY = e.clientY - this.rect.top;
                this.drawLine(e);
                console.log("start drawing")
            } else {
                // alert('Please load canvas before plotting')
                this.message = 'Please load canvas before plotting.';
            }



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

                    this.ctx.strokeStyle = "darkred";//#249701 darkred
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
    /* height: 500px; */
    position: relative;
    min-height: 80vh;

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