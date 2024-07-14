<template>
  <div class="auth">
    <div class="content">
      <div class="auth-wrapper">
        <!-- Holds logo and icon -->
        <div class="logo">
          <img :src="bucketImage" alt="axolotlImage" draggable="false" />
          <h1 class="readex-pro">BucketTest</h1>
        </div>
        <!-- Holds email and password input -->
        <form class="auth-form">
          <input class="form-input interactable" type="text" placeholder="Email" data-type="input" />
          <input class="form-input interactable" type="password" placeholder="Password" data-type="input" />
        </form>
        <!-- Holds auth button -->
        <button v-if="isSignup" class="form-button readex-pro interactable">Sign Up</button>
        <button v-else class="form-button readex-pro interactable">Log In</button>
        <!-- Holds prompt to switch auth mode -->
        <div class="auth-switch">
          <p>
            {{
              isSignup ? "Already have an account?" : "Don't have an account?"
            }}
          </p>
          <a class="interactable" href="#" @click.prevent="toggleAuthMode">
            &nbsp;{{ isSignup ? "Log in." : "Sign up." }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import DarkModeToggle from "@/components/DarkModeToggle.vue";

export default {
  name: "AuthView",
  components: {
    DarkModeToggle,
  },
  data() {
    return {
      isSignup: false,
      user_id: "",
      password: "",
    };
  },
  methods: {
    toggleAuthMode() {
      this.isSignup = !this.isSignup;
    },
  },
  computed: {
    ...mapGetters(["isDarkMode"]),
    bucketImage() {
      return this.isDarkMode
        ? require("@/assets/bucket.png")
        : require("@/assets/bucket.webp");
    },
  },
};
</script>

<style scoped>
.auth {
  max-width: 100%;
  max-height: 100%;
  width: 100dvw;
  height: 100dvh;

  overflow: hidden;

  background-color: var(--primary);
  background-image: radial-gradient(circle at 1px 1px,
      var(--dots) 0.1dvw,
      transparent 0);
  background-size: 2.4dvw 2.4dvw;
  color: var(--primary-text);

  font-size: 14px;
}

.content {
  width: 100%;
  height: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-wrapper {
  height: 420px;
  width: 380px;

  background: var(--primary);

  backdrop-filter: blur(0.1dvw);
  box-shadow: 0 1dvw 2dvw 0 var(--shadow);
  padding: 32px;
  border-radius: 32px;
  box-sizing: border-box;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;

}

.auth-form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-input {
  height: 50px;
  width: 100%;

  background: var(--secondary);
  border: transparent;
  outline: 2px solid var(--terciary);

  border-radius: 50px;
  padding: 25px;
  box-sizing: border-box;
}

.form-input+.form-input {
  margin-top: 25px;
}

input:focus {
  outline: 2px solid var(--identity);
}

input::placeholder {
  color: var(--placeholder);
}

.form-button {
  width: 100%;
  height: 50px;

  background: var(--button);
  color: var(--primary-text-inverted);

  border-radius: 50px;
  border: transparent;

  margin-top: 25px;

  cursor: pointer;
  font-weight: 700;

}

.form-button:hover {
  background: var(--identity);
}

.auth-switch {
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;

  box-sizing: border-box;

  p {
    color: var(--primary-text);
  }

  a {
    color: var(--identity);
    text-decoration: none;
    font-weight: 700;
  }
}

.logo {
  display: flex;
  flex-direction: row;
  flex: 1;
  justify-content: center;
  align-items: center;

  padding: 25px 0;
  box-sizing: border-box;

  overflow: hidden;

  img {
    max-height: 100%;
  }
}

h1 {
  margin-left: 4px;

  font-size: 32px;
  font-weight: 800;
}
</style>
