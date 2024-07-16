<template>
    <div class="pushNotification" :class="{ 'drop-in': visible }">
        <strong>{{ code }}:&nbsp;</strong>
        <p>{{ body }}</p>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useNotificationStore } from '@/stores/notification-store';

export default {
    name: "PushNotification",
    setup() {
        const notiStore = useNotificationStore();

        return {
            body: computed(() => notiStore.getBody),
            code: computed(() => notiStore.getCode),
            visible: computed(() => notiStore.getVisible)
        };
    }
}
</script>
<style scoped>
.pushNotification {
    color: var(--primary-text);
    background-color: var(--primary);
    height: fit-content;
    width: 380px;
    border-radius: 32px;
    font-size: 14px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
    padding: 0px 32px;
    text-align: justify;
    text-overflow: ellipsis;
    box-shadow: 0 1dvw 2dvw 0 var(--shadow);
    transform: translateY(-20dvh);
    transition: transform 0.4s cubic-bezier(0.075, 0.82, 0.165, 1);
}

.drop-in {
    transform: translateY(0dvh);
    transition: transform 0.6s cubic-bezier(0.075, 0.82, 0.165, 1)
}

@keyframes dropIn {
    0% {
        transform: translateY(-20dvh);
    }

    100% {
        transform: translateY(0px);
    }
}

strong {
    color: var(--identity);
}
</style>