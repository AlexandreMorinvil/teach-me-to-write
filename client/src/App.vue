<template>
  <div>
    <ChineseCharacterCanvas />
  </div>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import ChineseCharacterCanvas from './components/ChineseCharacterCanvas.vue';

export default {
  name: 'App',
  components: {
    ChineseCharacterCanvas,
  }
}
</script>

<style>
html {
  background-color: antiquewhite;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
