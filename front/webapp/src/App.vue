<template>
  <div :class="{ dark: isDarkMode, light: !isDarkMode }">
    <router-view style="position: fixed; overflow: hidden" />
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
import { mapGetters } from "vuex";
import DarkModeToggle from "./components/DarkModeToggle.vue";
import LogoutButton from "./components/LogoutButton.vue";

export default {
  components: {
    DarkModeToggle,
    LogoutButton,
  },
  data() {
    return {
      mouseX: 0,
      mouseY: 0,
      circleX: 0,
      circleY: 0,
      isCircleVisible: false,
      animationFrame: null,
      circleOpacity: 0.5,
      interacting: false,
      type: "",
    };
  },
  computed: {
    ...mapGetters(["isDarkMode"]),
    circleStyle() {
      return {
        transform: `translate(${this.circleX}px, ${this.circleY}px) scale(${this.interacting ? 2 : 1
          })`,
        opacity: this.isCircleVisible ? this.circleOpacity : 0,
      };
    },
    circleIcon() {
      switch (this.type) {
        default:
          return require("@/assets/nothing.png");
        case "input":
          return require("@/assets/italic.svg");
        case "link":
          return require("@/assets/link.svg");
      }
    },
  },
  methods: {
    updatePosition(event) {
      const interactable = event.target.closest(".interactable");
      const teleport = event.target.closest(".teleport");
      this.interacting = interactable !== null; // interacting ?

      if (this.interacting) {
        this.type = interactable.dataset.type;
      } else {
        this.type = "";
      }

      if (teleport) {
        const rect = interactable.getBoundingClientRect();
        this.mouseX = rect.left + rect.width / 2 - 10; // Adjusting for the circle radius
        this.mouseY = rect.top + rect.height / 2 - 10; // Adjusting for the circle radius
      } else {
        this.mouseX = event.clientX - 10; // Adjusting for the circle radius
        this.mouseY = event.clientY - 10; // Adjusting for the circle radius
      }

      if (!this.animationFrame) {
        this.animateCircle();
      }
    },
    animateCircle() {
      const stiffness = 0.4;
      const damping = 1;

      const deltaX = this.mouseX - this.circleX;
      const deltaY = this.mouseY - this.circleY;

      const velocityX = deltaX * stiffness;
      const velocityY = deltaY * stiffness;

      this.circleX += velocityX * damping;
      this.circleY += velocityY * damping;

      this.animationFrame = requestAnimationFrame(this.animateCircle);
    },
    hideCircle() {
      this.isCircleVisible = false;
      cancelAnimationFrame(this.animationFrame);
      this.animationFrame = null;
    },
    showCircle() {
      this.isCircleVisible = true;
      if (!this.animationFrame) {
        this.animateCircle();
      }
    },
  },
  mounted() {
    document.addEventListener("mousemove", this.updatePosition);
    document.addEventListener("mouseleave", this.hideCircle);
    document.addEventListener("mouseenter", this.showCircle);
  },
  beforeDestroy() {
    document.removeEventListener("mousemove", this.updatePosition);
    document.removeEventListener("mouseleave", this.hideCircle);
    document.removeEventListener("mouseenter", this.showCircle);
    cancelAnimationFrame(this.animationFrame);
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
  --error-bg: rgb(255, 248, 248);
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
  --error-bg: rgb(38, 34, 34);


  -error .circle {
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
</style>
