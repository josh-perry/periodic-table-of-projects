<template>
  <div>
    <h1>Periodic Table of Projects</h1>
    <PeriodicTable/>

    <ProjectsModal v-modal="modalOpen"/>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'

import PeriodicTable from "./components/PeriodicTable.vue"
import ProjectsModal from "./components/ProjectsModal.vue"

export default {
  data() {
    return {
      modalOpen: false
    }
  },
  methods: {
    toggleModal() {
      this.modalOpen = !this.modalOpen;
    }
  }
};
</script>
