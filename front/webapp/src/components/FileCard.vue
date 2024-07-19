<template>
  <div class="file-card">
    <div class="title-container">{{ truncatedFileName }}</div>
    <div class="preview">
      <img v-if="fileImage" :src="fileImage" alt="File Image" />
    </div>
    <div style="display: flex">
      <div style="width: fit-content; flex-direction: column">
        <div class="uploaded">Uploaded on: {{ formattedDate }}</div>
        <div class="size">Size: {{ formattedFileSize }}</div>
      </div>
      <div
        style="
          flex: 1;
          display: flex;
          justify-content: flex-end;
          align-items: flex-end;
          gap: 0 12px;
        "
      >
        <button class="button interactable teleport">
          <img
            :src="downloadImage"
            alt="themeImage"
            draggable="false"
            @click="handleDownload"
          />
        </button>
        <button class="button interactable teleport">
          <img
            :src="deleteImage"
            alt="themeImage"
            draggable="false"
            @click="handleDelete"
          />
        </button>
      </div>
    </div>
  </div>
</template>

<!--
file_name
upload_date
file_type
size
image
-->

<script>
import { computed, defineComponent } from "vue";
import { base64ToFile } from "@/utils/fileUtils";
import { useThemeStore } from "@/stores/theme-store";
import { deleteFile, downloadFile } from "@/utils/fileUtils";
import { useFileStore } from "@/stores/file-store";

export default defineComponent({
  props: {
    file: {
      type: Object,
      required: true,
    },
  },
  setup(props) {
    const themeStore = useThemeStore();
    const fileStore = useFileStore();

    const truncatedFileName = computed(() => {
      const parts = props.file.file_name.split("/");
      return parts.length > 1 ? parts.slice(1).join("/") : parts[0];
    });

    const formattedFileSize = computed(() => {
      const size = props.file.size;
      if (size < 1024) return `${size} bytes`;
      const i = Math.floor(Math.log(size) / Math.log(1024));
      const sizeUnits = ["bytes", "KB", "MB", "GB", "TB"];
      return (size / Math.pow(1024, i)).toFixed(2) + " " + sizeUnits[i];
    });

    const fileImage = computed(() => {
      if (props.file.image) {
        const file = base64ToFile(
          props.file.image,
          props.file.file_name,
          props.file.file_type
        );
        if (file) {
          return URL.createObjectURL(file);
        }
      }
      return null;
    });

    const formattedDate = computed(() => {
      return props.file.upload_date.substr(0, 10);
    });

    const downloadImage = computed(() => {
      return themeStore.get
        ? require("@/assets/downloadlight.svg")
        : require("@/assets/download.svg");
    });

    const deleteImage = computed(() => {
      return themeStore.get
        ? require("@/assets/deletelight.svg")
        : require("@/assets/delete.svg");
    });

    const handleDownload = async () => {
      const name = truncatedFileName.value; // Use the truncated name here
      try {
        const url = downloadFile(name);
        window.open(url, "_blank");
      } catch (e) {}
    };

    const handleDelete = async () => {
      const name = truncatedFileName.value; // Use the truncated name here
      try {
        await deleteFile(name);
        await fileStore.fetchFiles();
      } catch (error) {
        console.error("Failed to delete file:", error);
      }
    };

    return {
      truncatedFileName,
      formattedFileSize,
      fileImage,
      formattedDate,
      downloadImage,
      deleteImage,
      handleDownload,
      handleDelete,
    };
  },
});
</script>

<style scoped>
.file-card {
  color: var(--primary-text);
  position: relative;
  max-width: 100%;
  background-color: var(--primary);
  overflow: hidden;
  padding: 16px;
  border-radius: 16px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 8px 0 var(--shadow);
}

.title-container {
  font-size: 14px;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  text-overflow: ellipsis;
  text-wrap: nowrap;
  height: fit-content;
  overflow: hidden;
  box-sizing: border-box;
  padding-left: 8px;
}

.preview {
  width: 100%;
  height: 160px;
  background-color: var(--secondary);
  margin-top: 16px;
  margin-bottom: 16px;
  border-radius: 16px;
  overflow: hidden;
  img {
    width: 100%;
    height: 160px;
    object-fit: cover;
  }
}

.uploaded {
  font-size: 12px;
  color: var(--secondary-text);
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-bottom: 12px;
}

.size {
  font-size: 12px;
  color: var(--placeholder);
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.button {
  height: 32px;
  aspect-ratio: 1/1;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border: transparent;
  cursor: pointer;
  background-color: var(--primary);
  box-shadow: inset 0 4px 4px 0 var(--shadow);
}

.button:hover {
  background: var(--identity);

  img {
    filter: invert(100%);
  }
}
</style>
