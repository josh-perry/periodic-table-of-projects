export const state = () => ({
  elementName: '',
  projects: []
})

export const mutations = {
  async select (state, elementName) {
    state.elementName = elementName
    state.projects = await this.$http.$get(`${this.$config.baseUrl}/json/${elementName}.json`)
  },
  unselect (state) {
    state.elementName = ''
    state.projects = []
  }
}
