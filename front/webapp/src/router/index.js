import { createRouter, createWebHistory } from "vue-router";
import AuthView from "../views/AuthView.vue";

const routes = [
  {
    path: "/",
    name: "auth",
    component: AuthView,
  },
  {
    path: "/drive",
    name: "drive",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/DriveView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
