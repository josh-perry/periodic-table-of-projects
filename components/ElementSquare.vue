<template>
  <div class="element-square">
    <p>{{ name }}</p>
  </div>
</template>

<script>
export default {
  name: "ElementSquare",
  props: ["name", "projects"]
}
</script>

<style scoped>
.element-square {
  margin: auto;
  flex: 1 1 5.5%;

  border: 1px solid black;

  display: flex;
  align-items: center;
}

.element-square>p {
  margin-left: auto;
  margin-right: auto;
}

.element-square:before {
  content: "";
  margin-top: 100%;
}
</style>
