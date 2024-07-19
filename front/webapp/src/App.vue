<template>
  <div :class="{ dark: isDarkMode, light: !isDarkMode }">
    <router-view style="position: fixed; overflow: hidden" />
    <div class="notifications">
      <PushNotification />
    </div>
    <div class="sidebar">
      <DarkModeToggle />
      <LogoutButton />
    </div>
    <div class="circle" :style="circleStyle">
      <img :src="circleIcon" alt="" />
    </div>
  </div>
</template>

<script>
import { useThemeStore } from "@/stores/theme-store";
import { computed, ref, onMounted, onBeforeUnmount } from "vue";
import DarkModeToggle from "./components/DarkModeToggle.vue";
import LogoutButton from "./components/LogoutButton.vue";
import PushNotification from "./components/PushNotification.vue";

export default {
  components: {
    DarkModeToggle,
    LogoutButton,
    PushNotification,
  },
  setup() {
    const themeStore = useThemeStore();

    const mouseX = ref(0);
    const mouseY = ref(0);
    const circleX = ref(0);
    const circleY = ref(0);
    const isCircleVisible = ref(false);
    const animationFrame = ref(null);
    const circleOpacity = ref(0.5);
    const interacting = ref(false);
    const type = ref("");

    const circleStyle = computed(() => {
      return {
        transform: `translate(${circleX.value}px, ${circleY.value}px) scale(${
          interacting.value ? 2 : 1
        })`,
        opacity: isCircleVisible.value ? circleOpacity.value : 0,
      };
    });

    const circleIcon = computed(() => {
      switch (type.value) {
        default:
          return require("@/assets/nothing.png");
        case "input":
          return require("@/assets/italic.svg");
        case "link":
          return require("@/assets/link.svg");
        case "upload":
          return require("@/assets/upload.svg");
      }
    });

    const updatePosition = (event) => {
      const interactable = event.target.closest(".interactable");
      const teleport = event.target.closest(".teleport");
      interacting.value = interactable !== null;

      if (interacting.value) {
        type.value = interactable.dataset.type;
      } else {
        type.value = "";
      }

      if (teleport) {
        const rect = interactable.getBoundingClientRect();
        mouseX.value = rect.left + rect.width / 2 - 10; // Adjusting for the circle radius
        mouseY.value = rect.top + rect.height / 2 - 10; // Adjusting for the circle radius
      } else {
        mouseX.value = event.clientX - 10; // Adjusting for the circle radius
        mouseY.value = event.clientY - 10; // Adjusting for the circle radius
      }

      if (!animationFrame.value) {
        animateCircle();
      }
    };

    const animateCircle = () => {
      const stiffness = 0.4;
      const damping = 1;

      const deltaX = mouseX.value - circleX.value;
      const deltaY = mouseY.value - circleY.value;

      const velocityX = deltaX * stiffness;
      const velocityY = deltaY * stiffness;

      circleX.value += velocityX * damping;
      circleY.value += velocityY * damping;

      animationFrame.value = requestAnimationFrame(animateCircle);
    };

    const hideCircle = () => {
      isCircleVisible.value = false;
      cancelAnimationFrame(animationFrame.value);
      animationFrame.value = null;
    };

    const showCircle = () => {
      isCircleVisible.value = true;
      if (!animationFrame.value) {
        animateCircle();
      }
    };

    onMounted(() => {
      document.addEventListener("mousemove", updatePosition);
      document.addEventListener("mouseleave", hideCircle);
      document.addEventListener("mouseenter", showCircle);
    });

    onBeforeUnmount(() => {
      document.removeEventListener("mousemove", updatePosition);
      document.removeEventListener("mouseleave", hideCircle);
      document.removeEventListener("mouseenter", showCircle);
      cancelAnimationFrame(animationFrame.value);
    });

    return {
      themeStore,
      isDarkMode: computed(() => themeStore.get),
      circleStyle,
      circleIcon,
    };
  },
};
</script>

<style>
#app {
  font-family: sf-pro, -apple-system, BlinkMacSystemFont, "Helvetica Neue",
    Helvetica, Segoe UI, Arial, Roboto, "PingFang SC", "miui",
    "Hiragino Sans GB", "Microsoft Yahei", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100dvw;
  height: 100dvh;
  max-width: 100%;
  max-height: 100%;
}

button {
  user-select: none;
}

* {
  transition: background-color cubic-bezier(0.075, 0.82, 0.165, 1) 0.3s,
    color cubic-bezier(0.075, 0.82, 0.165, 1) 0.3s,
    outline cubic-bezier(0.075, 0.82, 0.165, 1) 0.3s,
    opacity cubic-bezier(0.075, 0.82, 0.165, 1) 0.3s,
    outline cubic-bezier(0.075, 0.82, 0.165, 1) 0.3s;
}

.light {
  --dots: rgba(180, 180, 200, 1);

  --primary-text: rgb(18, 18, 20);
  --secondary-text: rgb(38, 38, 40);
  --shadow: rgba(31, 38, 135, 0.2);

  --primary: rgb(255, 255, 255);
  --secondary: rgb(248, 248, 250);
  --terciary: rgb(230, 230, 240);
  --quaternary: rgb(225, 225, 238);

  --placeholder: rgb(171, 175, 186);
  --button: rgb(185, 188, 198);

  --primary-text-inverted: rgb(233, 233, 235);

  --identity: #345fdc;
  --identity-hover: #224dcf;

  --error: #dc5334;
  --error-outline: #dc5334;
  --error-bg: rgb(255, 245, 245);
}

.dark {
  --dots: rgba(180, 180, 200, 0.4);

  --primary-text: rgb(233, 233, 235);
  --secondary-text: rgb(200, 200, 202);
  --shadow: rgba(0, 0, 0, 0.6);

  --primary: rgb(28, 28, 30);
  --secondary: rgb(34, 34, 36);
  --terciary: rgb(44, 44, 46);
  --quaternary: rgb(64, 64, 66);

  --placeholder: rgb(105, 105, 110);
  --button: rgb(85, 85, 90);

  --primary-text-inverted: rgb(18, 18, 20);

  --identity: #ffc107;
  --identity-hover: #ebb106;

  --error: #dc5334;
  --error-outline: #b2533e;
  --error-bg: rgb(44, 34, 34);

  .circle {
    img {
      filter: invert(100%);
    }
  }
}

.circle {
  position: fixed;
  width: 20px;
  height: 20px;
  background-color: var(--identity);
  opacity: 20%;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0;
  transition: opacity 500ms linear, transform 100ms linear;
  display: flex;
  justify-content: center;
  align-items: center;

  img {
    width: 18px;
    aspect-ratio: 1/1;
  }
}

.sidebar {
  position: fixed;
  right: 0;
  height: 100%;
  background: transparent;
  box-sizing: border-box;
  padding: 2dvw;
  display: flex;
  flex-direction: column;
  gap: 24px 0;
}

.notifications {
  position: fixed;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: transparent;
  height: calc(45dvh - 210px);
  /* 50dvh - 210px, half page minus og auth box */
  pointer-events: none;
  overflow: hidden;
  box-sizing: border-box;
}
</style>
