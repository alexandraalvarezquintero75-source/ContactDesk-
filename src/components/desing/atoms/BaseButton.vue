<template>
  <button :class="['btn-circle', sizeClass, 'me-2']" @click="$emit('click')">
    <i v-if="icon" :class="icon"></i>
    <slot />
  </button>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  size: { type: String, default: "md" }, 
  icon: { type: String, default: null }, 
});

const sizeClass = computed(() =>
  props.size === "sm" ? "btn-sm" : props.size === "lg" ? "btn-lg" : "",
);
</script>

<style scoped>
.btn-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 1px solid #dee2e6;
  background-color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.btn-circle:hover {
  background-color: #f8f9fa;
}
</style>
