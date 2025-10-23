<template>
  <div class="d-flex justify-content-center gap-3 mt-4">
    <!-- Guardar -->
    <button
      type="button"
      class="btn btn-success rounded-pill px-4 py-2"
      @click="$emit('save')"
      title="Guardar"
    >
      Guardar
    </button>
    <button
      type="button"
      class="btn btn-secondary rounded-pill px-4 py-2"
      @click="$emit('cancel')"
      title="Cancelar"
    >
      Cancelar
    </button>
  </div>
</template>

<script setup>
defineProps({});
</script>
