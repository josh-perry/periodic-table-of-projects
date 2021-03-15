<template>
  <div>
    <h1>Periodic Table of Projects</h1>

    <div class="container">
      <PeriodicTable class="left"/>
      <ProjectsModal class="right"/>
    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

export default {};
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
}

.left {
  flex: 0 0 70%;
}

.right {
  flex: 0 0 25%;
  height: 90vh;
}
</style>
