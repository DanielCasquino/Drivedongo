<template>
  <div class="drive">
    <div class="content">
      <div class="bucket-wrapper">
        <div class="header readex-pro">
          <h1>File Explorer</h1>
        </div>
        <div class="explorer">
          <div
            class="files"
            @dragover.prevent="onDragOver"
            @dragleave="onDragLeave"
            @drop.prevent="onDrop"
            :class="{ 'drag-over': isDragOver }"
          >
            <!-- <FileUpload @file-uploaded="handleFileUploaded" />
            <div v-if="uploadedFileMetadata">
              <h3>File Metadata:</h3>
              <p><strong>Name:</strong> {{ uploadedFileMetadata.name }}</p>
              <p>
                <strong>Size:</strong> {{ uploadedFileMetadata.size }} bytes
              </p>
              <p><strong>Type:</strong> {{ uploadedFileMetadata.type }}</p>
              <h3>File Content:</h3>
              <pre>{{ uploadedFileBase64 }}</pre>
              <button
                class="interactable"
                @click="handleSubmit"
                data-type="upload"
              >
                Upload File
              </button>
            </div> -->
            <div v-for="file in loadedFiles" :key="file.name">
              <FileCard :file="file" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FileUpload from "@/components/FileUpload.vue";
import { useFileStore } from "@/stores/file-store";
import { ref, computed, onMounted } from "vue";
import FileCard from "@/components/FileCard.vue";
import { useNotificationStore } from "@/stores/notification-store";
import { sendFile } from "@/utils/fileUtils";

export default {
  components: {
    FileUpload,
    FileCard,
  },
  setup() {
    const fileStore = useFileStore();
    const notiStore = useNotificationStore();
    const isDragOver = ref(false);

    const uploadedFileMetadata = computed(() => fileStore.uploadedFileMetadata);
    const uploadedFileBase64 = computed(() => fileStore.uploadedFileBase64);
    const loadedFiles = computed(() => fileStore.loadedFiles);

    const handleFileUploaded = (payload) => {
      fileStore.setFileMetadata(payload.fileMetadata);
      fileStore.setFileBase64(payload.fileBase64);
    };

    const onDragOver = () => {
      isDragOver.value = true;
    };

    const onDragLeave = () => {
      isDragOver.value = false;
    };

    const onDrop = async (event) => {
      isDragOver.value = false;
      const file = event.dataTransfer.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = async (e) => {
          const base64 = e.target.result;
          fileStore.setFileBase64(base64);
          fileStore.setFileMetadata({
            name: file.name,
            size: file.size,
            type: file.type,
          });
          await handleSubmit();
        };
        reader.readAsDataURL(file);
      }
    };

    onMounted(() => {
      fileStore.fetchFiles();
    });

    const handleSubmit = async () => {
      try {
        await sendFile(uploadedFileMetadata.value, uploadedFileBase64.value);
        await fileStore.fetchFiles();
      } catch (e) {
        throw e;
      }
    };

    return {
      uploadedFileMetadata,
      uploadedFileBase64,
      loadedFiles,
      handleFileUploaded,
      handleSubmit,
      notiStore,
      isDragOver,
      onDragOver,
      onDragLeave,
      onDrop,
    };
  },
};
</script>

<style scoped>
.drive {
  max-width: 100%;
  max-height: 100%;
  width: 100dvw;
  height: 100dvh;

  overflow: hidden;

  background-color: var(--primary);
  background-image: radial-gradient(
    circle at 1dvw 1dvw,
    var(--dots) 0.1dvw,
    transparent 0
  );
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

.header {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  font-weight: 700;
  height: fit-content;
  box-sizing: border-box;
  padding: 2dvw;
  background-color: var(--primary);

  h1 {
    margin: 0;
    font-size: 32px;
  }

  h2 {
    margin: 0;
    font-size: var(--size-p);
    font-family: "sfpro", sans-serif;
    color: var(--placeholder);
    font-weight: 400;
  }
}

.bucket-wrapper {
  background: var(--primary);
  box-shadow: 0 8px 16px 0 var(--shadow);
  border-radius: 32px;
  height: 40dvw;
  width: 80dvw;
  box-sizing: border-box;

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  overflow: hidden;
}

.explorer {
  width: 100%;
  display: flex;
  flex: 1;
  overflow: hidden;
  background-color: var(--secondary);
}

.navbar {
  display: flex;
}

.files {
  width: 100%;
  height: 100%;
  padding: 32px;
  box-sizing: border-box;
  overflow: auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 16px;
  /* Adjust gap between items as needed */
  padding: 16px;
  /* Adjust padding as needed */
}

.files.drag-over {
  border: 2px dashed #aaa;
}
</style>
