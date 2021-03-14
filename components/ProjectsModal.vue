<template>
  <div class="modal">
    <p>{{ elementName }}</p>

    <div class="project-container">
      <div class="project" v-for="project in projects">
        <a :href="`https://github.com/${project.full_name}`">
          <img :src="`https://gh-card.dev/repos/${project.full_name}.svg?fullname=`">
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProjectsModal",
  computed: {
    elementName() {
      return this.$store.state.selectedElement.elementName;
    },
    projects() {
      return this.$store.state.selectedElement.projects;
    }
  }
};
</script>

<style scoped>
.modal {
}

.project-container {
  display: flex;
  flex-wrap: wrap;
}

.project {
  flex: 1;
  width: 50%;
}
</style>
