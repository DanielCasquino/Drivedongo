// store/index.js
import { createStore } from "vuex";

export default createStore({
  state: {
    isDarkMode: false,
  },
  mutations: {
    toggleDarkMode(state) {
      state.isDarkMode = !state.isDarkMode;
    },
    setDarkMode(state, value) {
      state.isDarkMode = value;
    },
  },
  actions: {
    toggleDarkMode({ commit }) {
      commit("toggleDarkMode");
    },
    setDarkMode({ commit }, value) {
      commit("setDarkMode", value);
    },
  },
  getters: {
    isDarkMode: (state) => state.isDarkMode,
  },
});
