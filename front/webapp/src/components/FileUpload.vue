<template>
  <div>
    <input type="file" @change="handleFileUpload" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      fileMetadata: null,
      fileEncodedBase64: null,
    };
  },
  methods: {
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        this.fileMetadata = {
          name: file.name,
          size: file.size,
          type: file.type,
        };
        const reader = new FileReader();
        reader.onload = (e) => {
          this.fileBase64 = e.target.result;
          this.$emit("file-uploaded", {
            fileMetadata: this.fileMetadata,
            fileBase64: this.fileBase64,
          });
        };
        reader.readAsDataURL(file); // Use readAsDataURL for binary files
      }
    },
  },
};
</script>
