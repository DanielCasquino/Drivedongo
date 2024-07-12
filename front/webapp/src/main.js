import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "normalize.css";
import "./assets/fonts/fonts.css";
import store from "./store";

const app = createApp(App);
app.use(store);
app.use(router);
app.mount("#app");
