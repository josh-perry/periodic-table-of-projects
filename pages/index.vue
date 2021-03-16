<template>
  <div>
    <h1>Periodic Table of Projects</h1>

    <div class="container">
      <PeriodicTable class="left" />
      <ProjectsModal class="right" />
    </div>
  </div>
</template>

<script lang="ts">
export default {}
</script>

<style>
html {
  background-color: #eeeeee;
}
</style>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
}

.left {
  flex: 1 1 60%;
}

.right {
  flex: 1 1 30%;
  height: 80vh;
  min-width: 400px;
}

h1 {
  margin: 16px;
}
</style>
