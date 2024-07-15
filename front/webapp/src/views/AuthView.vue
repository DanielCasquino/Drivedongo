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
        <form class="auth-form" @submit.prevent="handleSubmit">
          <input class="form-input interactable" :class="{ 'input-error': uidError }" @click="clearErrors" type="text"
            v-model="user_id" placeholder="Email" data-type="input" />
          <input class="form-input interactable" :class="{ 'input-error': passError }" @click="clearErrors"
            v-model="password" type="password" placeholder="Password" data-type="input" />
        </form>
        <!-- Holds auth button -->
        <button class="form-button readex-pro interactable" :class="{ 'button-disabled': !submitEnabled }"
          @click="handleSubmit" :disabled="!submitEnabled" type="submit" data-type="link">
          {{ isSignup ? "Sign Up" : "Log in" }}
        </button>
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
import { login, signup } from "@/utils/authUtils";

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
      submitEnabled: true,
      uidError: false,
      passError: false
    };
  },
  methods: {
    toggleAuthMode() {
      if (!this.submitEnabled) return;
      this.isSignup = !this.isSignup;
      this.error = false;
    },
    async handleSubmit() {
      try {
        if (!this.submitEnabled) return;
        else this.submitEnabled = false;
        this.uidError = false;
        this.passError = false;

        if (this.isSignup) {
          await signup(this.user_id, this.password);
        } else {
          await login(this.user_id, this.password);
        }
      }
      catch (e) {
        switch (e.statusCode) {
          case 400:
          case 403: this.passError = true;
          case 404: this.uidError = true; break;
          default: break;
        }
      }
      this.submitEnabled = true;
      // Prevent multiple submissions
    },
    clearErrors() {
      this.uidError = false;
      this.passError = false;
    }
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
  background-image: radial-gradient(circle at 1dvw 1dvw,
      var(--dots) 0.1dvw,
      transparent 0);
  background-size: 2dvw 2dvw;
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

  color: var(--primary-text);
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

.input-error {
  background: var(--error-bg);
  outline: 2px solid var(--error);
  animation: errorShake 0.3s cubic-bezier(0.075, 0.82, 0.165, 1);
  animation-fill-mode: forwards;
}

@keyframes errorShake {
  0% {
    transform: translateX(-1dvw);
  }

  33% {
    transform: translateX(1dvw)
  }

  66% {
    transform: translateX(-1dvw);
  }

  100% {
    transform: translateX(0dvw);
  }
}

.form-button {
  width: 100%;
  height: 50px;

  background: var(--identity);
  color: var(--primary-text-inverted);

  border-radius: 50px;
  border: transparent;

  margin-top: 25px;

  cursor: pointer;
  font-weight: 700;
}

.button-disabled {
  background: var(--button);
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
