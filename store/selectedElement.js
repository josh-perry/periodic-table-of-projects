export const state = () => ({
  elementName: ""
});

export const mutations = {
  select(state, elementName) {
    state.elementName = elementName;
  },
  unselect(state) {
    elementName = "";
  }
}
