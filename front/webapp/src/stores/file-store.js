import { defineStore } from "pinia";
import { listFiles } from "@/utils/fileUtils";

export const useFileStore = defineStore("file", {
  state: () => ({
    uploadedFileMetadata: null,
    uploadedFileBase64: null,
    loadedFiles: [],
  }),
  getters: {
    getUploadedMetadata: (state) => state.uploadedFileMetadata,
    getUploadedBase64: (state) => state.uploadedFileBase64,
    getFiles: (state) => state.loadedFiles,
  },
  actions: {
    setFileMetadata(fileMetadata) {
      this.uploadedFileMetadata = fileMetadata;
    },
    setFileBase64(fileBase64) {
      this.uploadedFileBase64 = fileBase64;
    },
    async fetchFiles() {
      try {
        const files = await listFiles();
        this.loadedFiles = files;
      } catch (e) {
        console.error("Error fetching files:", e);
      }
    },
    clear() {
      this.loadedFiles = null;
    },
  },
});
