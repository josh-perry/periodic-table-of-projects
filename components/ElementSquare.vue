<template>
  <div class="element-square" @click="select">
    <p>{{ element.symbol }}</p>
    <p>{{ element.count }}</p>
  </div>
</template>

<script>
export default {
  name: 'ElementSquare',
  props: {
    element: {
      type: Object,
      default: () => {
        return {
          symbol: '',
          count: 0
        }
      }
    }
  },
  methods: {
    select () {
      this.$store.dispatch('selectedElement/updateSelectedElement', this.element.name)
    }
  }
}
</script>

<style scoped>
.element-square {
  margin: auto;
  flex: 1 1 5.5%;

  border: 1px solid black;
  border-radius: 8px;

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
