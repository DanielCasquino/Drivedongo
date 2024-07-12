<template>
  <div class="home">
    <div class="content">
      <div class="auth-wrapper">
        <!-- Holds logo and icon -->
        <div class="logo">
          <img :src="bucketImage" alt="">
          <h1 class="readex-pro">Baldecito</h1>
        </div>
        <!-- Holds email and password input -->
        <form class="auth-form">
          <input class="form-input" type="text" placeholder="Email">
          </input>
          <input class="form-input" type="password" placeholder="Password">
          </input>
        </form>
        <!-- Holds auth button -->
        <button v-if="isSignup" class="form-button readex-pro" @click="toggleDark()">Sign Up</button>
        <button v-else class="form-button readex-pro">Log In</button>
        <!-- Holds prompt to switch auth mode -->
        <div class="prompt-wrapper">
          <p>{{ isSignup ? "Already have an account?" : "Don't have an account?" }}</p>
          <a href="#" @click.prevent="toggleAuthMode">
            &nbsp;{{ isSignup ? "Log in." : "Sign up." }}
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import DarkModeToggle from '@/components/DarkModeToggle.vue';


export default {
  name: 'HomeView',
  components: {
    DarkModeToggle
  },
  data() {
    return {
      isSignup: false,
      user_id: '',
      password: ''
    };
  },
  methods: {
    toggleAuthMode() {
      this.isSignup = !this.isSignup;
    },
  },
  computed: {
    ...mapGetters(['isDarkMode']),
    bucketImage() {
      return this.isDarkMode
        ? require('@/assets/bucket.png')
        : require('@/assets/bucket.webp');
    },
  },
}
</script>

<style scoped>
.home {
  width: 100dvw;
  height: 100dvh;
  max-width: 100%;
  max-height: 100%;
  overflow: hidden;
  background-color: var(--primary);
  background-image: radial-gradient(circle at 1px 1px, var(--primary-text) 0.7px, transparent 0);
  background-size: 30px 30px;
  color: var(--primary-text);
}

.content {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-wrapper {
  background: var(--primary);
  backdrop-filter: blur(0.1dvw);
  box-shadow: 0 8px 16px 0 var(--shadow);
  border-radius: 32px;
  height: 420px;
  width: 380px;
  box-sizing: border-box;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 32px;
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
  outline: 1.5px solid var(--terciary);
  border: transparent;
  border-radius: 64px;
  font-size: var(--size-p);
  padding: 25px;
  box-sizing: border-box;
}

.form-input+.form-input {
  margin-top: 25px;
}

input:focus {
  outline: 1.5px solid var(--identity);
}

input::placeholder {
  color: var(--placeholder);
}

.form-button {
  width: 100%;
  height: 50px;
  font-weight: 700;
  border-radius: 64px;
  border: transparent;
  cursor: pointer;
  margin-top: 25px;
  background: var(--identity);
  color: var(--primary-text-inverted);
}

.prompt-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  font-size: var(--size-p);

  p {
    color: var(--primary-text);
  }

  a {
    text-decoration: none;
    color: var(--identity);
    font-weight: 700;
  }

  box-sizing: border-box;
}

.logo {
  display: flex;
  flex-direction: row;
  flex: 1;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  overflow: hidden;
  padding: 25px 0;

  img {
    max-height: 100%;
  }
}

h1 {
  font-size: var(--size-h1);
  margin-left: 4px;
  font-weight: 800;
}
</style>
