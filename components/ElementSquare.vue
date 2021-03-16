<template>
  <div :title="`${element.name} (${element.count} projects)`" class="element-square" :class="{ 'element-selected': selected }" @click="select">
    <small>{{ element.count }}</small>
    <p>{{ element.symbol }}</p>
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
  computed: {
    selected () {
      return this.$store.state.selectedElement.elementName === this.element.name
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
  border: 2px solid black;/*rgb(10, 106, 215);*/
  border-radius: 4px;

  user-select: none;
  cursor: pointer;

  background: #ffffff;
}

.element-square>p {
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  font-weight: bold;

  margin-top: 8px;
  margin-bottom: 12px;
}

.element-square>small {
  margin-left: 4px;
}

.element-square:before {
  content: "";
  padding-top: 100%;
}

.element-selected {
  background: rgb(10, 106, 215);
  border-radius: 4px;
  color: #ffffff;
}
</style>
