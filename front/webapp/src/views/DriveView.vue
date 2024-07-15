<template>
  <div class="drive">
    <div class="content">
      <div class="bucket-wrapper">
        <div class="header readex-pro">
          <h1>user@utec.edu.pe</h1>
        </div>
        <div class="explorer">
          <div class="navbar"></div>
          <div class="files">
            <FileUpload @file-uploaded="handleFileUploaded" />
            <div v-if="uploadedFileMetadata">
              <h3>File Metadata:</h3>
              <p><strong>Name:</strong> {{ uploadedFileMetadata.name }}</p>
              <p>
                <strong>Size:</strong> {{ uploadedFileMetadata.size }} bytes
              </p>
              <p><strong>Type:</strong> {{ uploadedFileMetadata.type }}</p>
              <h3>File Content:</h3>
              <pre>{{ uploadedFileBase64 }}</pre>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import FileCard from "@/components/FileCard.vue";
import FileUpload from "@/components/FileUpload.vue";

export default {
  components: {
    FileCard,
    FileUpload,
  },
  data() {
    return {
      loadedFiles: [],
      selectedFile: null,
      uploadedFileMetadata: null,
      uploadedFileBase64: null,
    };
  },
  methods: {
    handleFileUploaded(payload) {
      this.uploadedFileMetadata = payload.fileMetadata;
      this.uploadedFileBase64 = payload.fileBase64;
    },
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

.bucket-wrapper {
  background: var(--secondary);
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

.explorer {
  width: 100%;
  display: flex;
  flex: 1;
  overflow: hidden;
}

.navbar {
  display: flex;
}

.files {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 32px;
  gap: 8vmin;
  overflow: auto;
}
</style>
