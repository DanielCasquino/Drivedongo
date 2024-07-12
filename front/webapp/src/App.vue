<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <div :class="{ dark: isDarkMode, light: !isDarkMode }">
    <div class="absoluteOverlay">
      <DarkModeToggle />
    </div>
    <router-view />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import DarkModeToggle from './components/DarkModeToggle.vue';

export default {
  components: {
    DarkModeToggle,
  },
  computed: {
    ...mapGetters(['isDarkMode']),
  },
};
</script>


<style>
#app {
  font-family: sfpro, -apple-system, BlinkMacSystemFont, "Helvetica Neue", Helvetica, Segoe UI, Arial, Roboto, "PingFang SC", "miui", "Hiragino Sans GB", "Microsoft Yahei", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  --size-p: 13px;
  --size-h1: 28px;
  width: 100dvw;
  height: 100dvh;
  max-width: 100%;
  max-height: 100%;
}

* {
  font-family: inherit;
  color: inherit;
  font-size: inherit;
  font-weight: inherit;
  transition: all cubic-bezier(0.075, 0.82, 0.165, 1) 0.3s;
}

.light {
  --primary-text: rgb(18, 18, 20);
  --secondary-text: rgb(38, 38, 40);
  --shadow: rgba(31, 38, 135, 0.2);

  --primary: rgb(255, 255, 255);
  --secondary: rgb(250, 250, 252);
  --terciary: rgb(233, 234, 240);
  --quaternary: rgb(231, 232, 238);

  --placeholder: rgb(171, 175, 186);
  --button: rgb(185, 188, 198);

  --primary-text-inverted: rgb(233, 233, 235);

  --identity: #345FDC;
}

.dark {
  --primary-text: rgb(233, 233, 235);
  --secondary-text: rgb(200, 200, 202);
  --shadow: rgba(0, 0, 0, 0.6);

  --primary: rgb(40, 40, 40);
  --secondary: rgb(28, 28, 30);
  --terciary: rgb(58, 58, 60);
  --quaternary: rgb(60, 61, 67);

  --placeholder: rgb(105, 105, 110);
  --button: rgb(85, 85, 90);

  --primary-text-inverted: rgb(18, 18, 20);
  --identity: #FFC107;
}

.absoluteOverlay {
  position: absolute;
  height: 100%;
  width: 100%;
  background: transparent;
}
</style>
