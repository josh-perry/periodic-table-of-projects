<template>
  <div class="element-square" />
</template>

<script>
export default {
  name: 'ElementSquare'
}
</script>

<style scoped>
.element-square {
  margin: auto;
  flex: 1 1 5.5%;

  display: flex;
}

.element-square:before {
  content: "";
  margin-top: 100%;
}
</style>
