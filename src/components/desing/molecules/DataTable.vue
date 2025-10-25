<template>
  <div class="table-responsive shadow-sm rounded">
    <table class="table table-striped table-hover align-middle mb-0">
      <thead>
        <tr>
          <!-- Columna de selección -->
          <th class="text-center">
            <input
              type="checkbox"
              v-model="selectAll"
              @change="toggleSelectAll"
            />
          </th>
          <!-- Columnas dinámicas -->
          <th v-for="col in columns" :key="col.key">
            <i v-if="col.icon" :class="col.icon" class="me-2"></i>
            {{ col.label }}
          </th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(row, index) in data || []" :key="index">
          <!-- Checkbox de selección -->
          <td class="text-center">
            <input type="checkbox" v-model="selectedRows" :value="row" />
          </td>
          <!-- Celdas dinámicas -->
          <td v-for="col in columns" :key="col.key">{{ row[col.key] }}</td>
        </tr>

        <tr v-if="!data || data.length === 0">
          <td :colspan="columns.length + 1" class="text-center py-4">
            No hay datos disponibles
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
  columns: { type: Array, required: true },
  data: { type: Array, required: true, default: () => [] },
});

const emit = defineEmits(["update:selected"]);
// Estados
const selectedRows = ref([]);
const selectAll = ref(false);

// Seleccionar/deseleccionar todos
const toggleSelectAll = () => {
  if (selectAll.value) {
    selectedRows.value = [...props.data];
  } else {
    selectedRows.value = [];
  }
};

// Mantener sincronizado el "select all"
watch(selectedRows, (newVal) => {
  selectAll.value =
    newVal.length === props.data.length && props.data.length > 0;
  emit("update:selected", newVal);
});
</script>
