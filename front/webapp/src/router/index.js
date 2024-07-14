import { createRouter, createWebHistory } from "vue-router";
import AuthView from "../views/AuthView.vue";
import { checkAuth } from "@/utils/authUtils";
import DriveView from "@/views/DriveView.vue";


const routes = [
  {
    path: "/",
    name: "auth",
    component: AuthView,
    meta: {requiresAuth: false}
  },
  {
    path: "/drive",
    name: "drive",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: DriveView,
    meta: {requiresAuth: true}
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  console.log("Loading " + from.name + " to " + to.name)
  if (to.meta.requiresAuth) {
    const isAuthenticated = await checkAuth();
    if (!isAuthenticated) {
      next({
        path: "/",
        query: { redirect: to.fullPath },
      });
      return;
    }
  } else if (to.path === "/") {
    const isAuthenticated = await checkAuth();
    if (isAuthenticated) {
      next({ path: "/drive" });
      return;
    }
  }
  next();
});

export default router;
