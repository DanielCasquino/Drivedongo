import { defineStore } from "pinia";

export const useThemeStore = defineStore("theme", {
  state: () => ({
    isDarkMode: false,
  }),
  getters: {
    get: (state) => state.isDarkMode,
  },
  actions: {
    toggle() {
      this.isDarkMode = !this.isDarkMode;
    },
    set(value) {
      this.isDarkMode = value;
    },
  },
});
