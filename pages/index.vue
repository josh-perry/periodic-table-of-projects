<template>
  <div>
    <a href="#">
      <header>
        <h1>Periodic Table of Projects</h1>
      </header>
    </a>

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
header {
  background: black;
  color: white;
}

a {
  text-decoration: none;
}

header>h1 {
  padding: 16px;
}

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
</style>
