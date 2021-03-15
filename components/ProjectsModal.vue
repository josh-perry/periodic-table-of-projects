<template>
  <div class="modal">
    <p>{{ elementName }}</p>

    <div class="project-container">
      <div v-for="project in projects" :key="project.id" class="project">
        <a :href="`https://github.com/${project.full_name}`">
          <img :src="`https://gh-card.dev/repos/${project.full_name}.svg?fullname=`">
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectsModal',
  computed: {
    elementName () {
      return this.$store.state.selectedElement.elementName
    },
    projects () {
      return this.$store.state.selectedElement.projects
    }
  }
}
</script>

<style scoped>
.modal {
  overflow: scroll;
}

.project-container {
}

.project {
  width: 100%;
  margin: 10px;
}
</style>
