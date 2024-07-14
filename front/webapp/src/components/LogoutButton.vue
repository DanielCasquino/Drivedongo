<template>
  <button
    :class="[
      'button interactable teleport',
      { dark: isDarkMode, light: !isDarkMode },
    ]"
    @click="doLogout"
  >
    <img :src="themeImage" alt="themeImage" draggable="false" />
  </button>
</template>

<script>
import { mapGetters } from "vuex";
import { logout } from "@/utils/authUtils";

export default {
  computed: {
    ...mapGetters(["isDarkMode"]),
    themeImage() {
      return this.isDarkMode
        ? require("@/assets/logoutlight.svg")
        : require("@/assets/logout.svg");
    },
  },
  methods: {
    doLogout() {
      logout();
    },
  },
};
</script>

<style scoped>
.button {
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
