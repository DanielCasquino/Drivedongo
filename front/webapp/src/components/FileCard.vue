<template>
  <div class="card-wrapper">

  </div>
</template>

<script>
export default {
  name: "FileCard",
  setup() {
    return {
      name: "File",
      date: "DD-MM-YYYY",
      type: "txt"
    }
  }
}
</script>

<style scoped>
.card-wrapper {
  border-radius: 32px;
  height: 240px;
  width: 240px;
  outline: 2px solid var(--terciary);
  background-color: var(--secondary);
  box-sizing: border-box;
}
</style>
