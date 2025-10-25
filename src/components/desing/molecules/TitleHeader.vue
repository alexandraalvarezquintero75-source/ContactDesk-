<template>
  <div
    class="d-flex align-items-center gap-2"
    :class="
      position === 'center'
        ? 'justify-content-center'
        : 'justify-content-start ms-4'
    "
  >
    <!-- Slot para el icono o logo -->
    <slot name="icon-header"></slot>

    <!-- Título -->
    <small :class="['fs-4 text-center', color]">
      {{ title }}
    </small>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, required: true },
  position: { type: String, default: "center" },
  color: { type: String, default: "text-primary" }, 
});
</script>
