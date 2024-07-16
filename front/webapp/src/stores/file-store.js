import { defineStore } from "pinia";

export const useFileStore = defineStore("file", {
  state: () => ({
    uploadedFileMetadata: null,
    uploadedFileBase64: null,
  }),
  actions: {
    setFileMetadata(fileMetadata) {
      this.uploadedFileMetadata = fileMetadata;
    },
    setFileBase64(fileBase64) {
      this.uploadedFileBase64 = fileBase64;
    },
  },
});
