<template>
  <button :class="['button interactable teleport', { dark: isDarkMode, light: !isDarkMode }]" @click="toggleDarkMode">
    <img :src="themeImage" alt="themeImage" draggable="false" />
  </button>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["isDarkMode"]),
    themeImage() {
      return this.isDarkMode
        ? require("@/assets/lightmode.svg")
        : require("@/assets/darkmode.svg");
    },
  },
  methods: {
    ...mapActions(["toggleDarkMode"]),
  },
};
</script>

<style scoped>
.button {
  position: fixed;
  top: 2dvw;
  right: 2dvw;
  aspect-ratio: 1/1;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border: transparent;
  cursor: pointer;
  background: var(--primary);
  box-shadow: 0 4px 8px 0 var(--shadow);
}

.button:hover {
  background: var(--identity);

  img {
    filter: invert(100%);
  }
}
</style>
