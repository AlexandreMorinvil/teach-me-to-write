<template>
    <div class="canvas-container">
      <canvas
        ref="canvas"
        class="drawing-canvas"
        @mousedown="startDrawing"
        @mousemove="draw"
        @mouseup="stopDrawing"
        @mouseleave="stopDrawing"
        @touchstart.prevent="startDrawing"
        @touchmove.prevent="draw"
        @touchend.prevent="stopDrawing"
      ></canvas>
      <div class="controls">
        <button @click="clearCanvas">清除</button>
        <button @click="saveCanvas">送出</button>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from "vue";
  
  export default {
    name: "ChineseCharacterCanvas",
    setup() {
      const canvas = ref(null);
      const ctx = ref(null);
      const isDrawing = ref(false);
      const lastPos = ref({ x: 0, y: 0 });
  
      const getMousePos = (event) => {
        const rect = canvas.value.getBoundingClientRect();
        return {
          x: event.clientX - rect.left,
          y: event.clientY - rect.top,
        };
      };
  
      const getTouchPos = (event) => {
        const rect = canvas.value.getBoundingClientRect();
        const touch = event.touches[0];
        return {
          x: touch.clientX - rect.left,
          y: touch.clientY - rect.top,
        };
      };
  
      const startDrawing = (event) => {
        isDrawing.value = true;
        const pos =
          event.type.includes("mouse")
            ? getMousePos(event)
            : getTouchPos(event);
        lastPos.value = pos;
      };
  
      const draw = (event) => {
        if (!isDrawing.value) return;
  
        const pos =
          event.type.includes("mouse")
            ? getMousePos(event)
            : getTouchPos(event);
  
        ctx.value.beginPath();
        ctx.value.moveTo(lastPos.value.x, lastPos.value.y);
        ctx.value.lineTo(pos.x, pos.y);
        ctx.value.stroke();
        lastPos.value = pos;
      };
  
      const stopDrawing = () => {
        isDrawing.value = false;
      };
  
      const clearCanvas = () => {
        ctx.value.clearRect(0, 0, canvas.value.width, canvas.value.height);
      };
  
      const saveCanvas = () => {
        const dataURL = canvas.value.toDataURL("image/png");
        const link = document.createElement("a");
        link.download = "drawing.png";
        link.href = dataURL;
        link.click();
      };
  
      onMounted(() => {
        canvas.value.width = 600;
        canvas.value.height = 600;
        ctx.value = canvas.value.getContext("2d");
        ctx.value.lineWidth = 10;
        ctx.value.strokeStyle = "black";
        ctx.value.lineCap = "round";
      });
  
      return {
        canvas,
        startDrawing,
        draw,
        stopDrawing,
        clearCanvas,
        saveCanvas,
      };
    },
  };
  </script>
  
  <style scoped>
  .canvas-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .drawing-canvas {
    background-color: white;
    border: 1px solid #ccc;
    touch-action: none;
  }
  
  .controls {
    margin-top: 10px;
    display: flex;
    gap: 10px;
  }
  
  button {
    padding: 8px 16px;
    font-size: 16px;
    cursor: pointer;
    border: none;
    border-radius: 4px;
    background-color: #007bff;
    color: white;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>