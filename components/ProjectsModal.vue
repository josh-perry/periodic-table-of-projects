<template>
  <div class="modal-container">
    <h2>{{ elementName }}</h2>

    <div class="modal">
      <div class="project-container">
        <div v-for="project in projects" :key="project.id" class="project">
          <a class="project-card" :href="`https://github.com/${project.full_name}`">
            <img :src="`https://gh-card.dev/repos/${project.full_name}.svg?fullname=`">
          </a>
        </div>
      </div>
    </div>

    <div class="button-container">
      <a class="button" :href="results_link">
        <span>See all results on GitHub</span>
      </a>
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
    },
    results_link() {
      const searchQuery = `in:name ${this.elementName}`;
      return `https://github.com/search?q=${encodeURIComponent(searchQuery)}`
    }
  }
}
</script>

<style scoped>
h2 {
  text-align: center;
  background: black;
  color: white;
}

.modal-container {
  display: flex;
  flex-direction: column;
  margin: 30px;
  background-color: #eeeeee;
  border: solid 2px black;
  border-radius: 4px;
}

.modal-container>p {
  flex: 1 1 5%;
}

.modal-container>.modal {
  flex: 1 1 90%;
}

.button-container {
  flex: 1 1 5%;
}

a.button {
  appearance: button;

  text-align: center;

  text-decoration: none;
  background-color: rgb(10, 106, 215);
  color: white;

  display: table;

  width: 100%;
  height: 100%;
}

a>span {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
}

.modal {
  height: 80vh;
  overflow: scroll;
}

.project-container {
}

.project {
  width: 100%;
  margin: 10px;
}
</style>
