export const state = () => ({
  elementName: '',
  projects: []
})

export const mutations = {
  setElementName (state, elementName) {
    state.elementName = elementName
  },
  setProjects (state, projects) {
    state.projects = projects
  },
  unselect (state) {
    state.elementName = ''
    state.projects = []
  }
}

export const actions = {
  async updateSelectedElement (context, elementName) {
    context.commit('setElementName', elementName)

    const projects = await this.$http.$get(`${this.$config.baseUrl}/json/${elementName}.json`)
    context.commit('setProjects', projects)
  }
}
