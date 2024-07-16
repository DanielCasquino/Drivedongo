<template>
  <button :class="[
    'button interactable teleport',
    { dark: isDarkMode, light: !isDarkMode },
  ]" @click="doLogout">
    <img :src="themeImage" alt="themeImage" draggable="false" />
  </button>
</template>

<script>
import { useThemeStore } from "@/stores/theme-store";
import { computed } from 'vue';
import { logout } from "@/utils/authUtils";

export default {
  setup() {
    const themeStore = useThemeStore();

    const themeImage = computed(() =>
      themeStore.get
        ? require('@/assets/logoutlight.svg')
        : require('@/assets/logout.svg')
    );

    const isDarkMode = computed(() => themeStore.get);

    const doLogout = () => {
      logout();
    };

    return {
      isDarkMode,
      themeImage,
      doLogout,
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
