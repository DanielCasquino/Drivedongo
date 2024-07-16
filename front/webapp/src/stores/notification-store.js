import { defineStore } from "pinia";

export const useNotificationStore = defineStore("notification", {
  state: () => ({
    visible: false,
    code: "000",
    body: "There's nothing to see here!",
  }),
  getters: {
    getVisible: (state) => state.visible,
    getCode: (state) => state.code,
    getBody: (state) => state.body,
  },
  actions: {
    show(code, body) {
      this.code = code;
      this.body = body;
      this.visible = true;
      setTimeout(() => {
        this.visible = false;
      }, 4000);
    },
  },
});
