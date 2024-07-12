<!-- components/DarkModeToggle.vue -->
<template>
    <button :class="['button', { dark: isDarkMode, light: !isDarkMode }]" @click="toggleDarkMode">
        <img :src="themeImage" alt="">
    </button>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
    computed: {
        ...mapGetters(['isDarkMode']),
        themeImage() {
            return this.isDarkMode
                ? require('@/assets/lightmode.svg')
                : require('@/assets/darkmode.svg');
        },
    },
    methods: {
        ...mapActions(['toggleDarkMode']),
    },
};
</script>

<style scoped>
.button {
    position: absolute;
    top: 1dvw;
    right: 1dvw;
    aspect-ratio: 1/1;
    border-radius: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border: transparent;
    cursor: pointer;
    background: var(--primary);
    box-shadow: 0 4px 8px 0 var(--shadow);
}

.light {
    --primary-text: rgb(18, 18, 20);
    --secondary-text: rgb(38, 38, 40);
    --shadow: rgba(31, 38, 135, 0.2);

    --primary: rgb(255, 255, 255);
    --secondary: rgb(250, 250, 252);
    --terciary: rgb(233, 234, 240);
    --quaternary: rgb(231, 232, 238);

    --placeholder: rgb(171, 175, 186);
    --button: rgb(185, 188, 198);

    --primary-text-inverted: rgb(233, 233, 235);

    --identity: #345FDC;
}

.dark {
    --primary-text: rgb(233, 233, 235);
    --secondary-text: rgb(200, 200, 202);
    --shadow: rgba(0, 0, 0, 0.6);

    --primary: rgb(40, 40, 40);
    --secondary: rgb(28, 28, 30);
    --terciary: rgb(58, 58, 60);
    --quaternary: rgb(60, 61, 67);

    --placeholder: rgb(105, 105, 110);
    --button: rgb(85, 85, 90);

    --primary-text-inverted: rgb(18, 18, 20);
    --identity: #FFC107;
}
</style>