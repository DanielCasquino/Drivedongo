<template>
  <button :class="['button interactable teleport', { dark: themeStore.get, light: !themeStore.get }]"
    @click="themeStore.toggle">
    <img :src="themeImage" alt="themeImage" draggable="false" />
  </button>
</template>

<script>
import { useThemeStore } from "@/stores/theme-store";
import { computed } from 'vue';

export default {
  name: "DarkModeToggle",
  setup() {
    const themeStore = useThemeStore();

    const themeImage = computed(() =>
      themeStore.get
        ? require('@/assets/lightmode.svg')
        : require('@/assets/darkmode.svg')
    );

    return {
      themeStore,
      themeImage,
    };
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
