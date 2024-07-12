<template>
  <div class="about">
    <div class="content">
      <div class="bucket-wrapper">
        <div class="header readex-pro">
          <h1>user@utec.edu.pe</h1>
          <h2>2MB of 100MB used</h2>
        </div>
        <div class="bucket-content"></div>
      </div>
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
.about {
  width: 100dvw;
  height: 100dvh;
  max-width: 100%;
  max-height: 100%;
  overflow: hidden;
  background-color: var(--primary);
  background-image: radial-gradient(circle at 1px 1px, var(--primary-text) 0.7px, transparent 0);
  background-size: 30px 30px;
  color: var(--primary-text);
}

.content {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.bucket-wrapper {
  background: var(--primary);
  backdrop-filter: blur(0.1dvw);
  box-shadow: 0 8px 16px 0 var(--shadow);
  border-radius: 32px;
  height: 540px;
  width: 1080px;
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
  font-size: var(--size-h1);
  height: fit-content;
  box-sizing: border-box;
  padding: 20px 40px 20px 40px;

  h1 {
    margin: 0;
    margin-bottom: 10px;
    font-size: var(--size-h1);
  }

  h2 {
    margin: 0;
    font-size: var(--size-p);
    font-family: 'sfpro', sans-serif;
    color: var(--placeholder);
    font-weight: 400;
  }
}

.bucket-content {
  width: 100%;
  display: flex;
  flex: 1;
  background: aliceblue;
}
</style>