<template>
    <div class="image-container">

        <!-- <img src="../assets/R134_p_h_diagram.svg" alt="Background" @load="adjustCanvasSize"> -->
        <!-- <img src="/images/R134_p_h_diagram.svg" alt="Background"> -->
        <canvas ref="canvas" @mousedown="startDrawing" @mouseup="endDrawing" @mousemove="drawLine"
            @mouseout="endDrawing" width="550" height="400"></canvas>
        <div>
            <button type="button" class="btn btn-primary" @click="clearLine">Clear</button>
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
        this.$nextTick(() => {
            const canvas = this.$refs.canvas;
            canvas.width = 550;
            canvas.height = 400;
        });
    },
    methods: {
        // drawing lines function
        startDrawing(e) {
            this.drawing = true;
            const rect = this.$refs.canvas.getBoundingClientRect();
            this.startX = e.clientX - rect.left;
            this.startY = e.clientY - rect.top;
            this.drawLine(e);
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
};
</script>

<style>
.image-container {
    display: inline;
}

.image-container canvas {
    background: url(../assets/Chart-p-h-R134a-1.png);
    background-size: 100% 100%;
    top: 0;
    left: 0;
}
</style>