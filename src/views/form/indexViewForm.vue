<template>
<div class="container-fluid">
    <div class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3"
    >
<TitleHeader title="Formulario prueba" position="start" color="text-success">
    <template #icon-header>
        <div class="d-flex align-items-center gap-2">
            <i class="bi bi-journal-text fs-3"></i>
            <NewGoalIcon width="40" height="40" />
        </div>
    </template>
</TitleHeader>
    
<div class="d-flex flex-wrap gap-2">
<AccionButtons
/>
</div>
    </div>
</div>

</template>
<script setup>
import TitleHeader from '@/components/desing/molecules/TitleHeader.vue'
import AccionButtons from '@/components/desing/molecules/AccionButtons.vue';
import { useRouter } from 'vue-router';
const router= useRouter();


const goForm=()=>{
    router.push({name:'form-forms'})
}

</script>
<style scoped>
div {
  border: 1px dashed #ccc;
  padding: 10px;
  margin: 5px;
  position: relative;
}

div::before {
  content: attr(class);
  position: absolute;
  top: 0;
  top: -14px; 
  left: 0;
  background: rgba(0,0,0,0.75);
  color: #fff;
  font-size: 10px;
  padding: 2px 4px;
  border-radius: 0 0 4px 0;
  opacity: 0; /* 👈 oculto por defecto */
  pointer-events: none;
  transition: opacity 0.2s;
}

div:hover::before {
  opacity: 1; /* 👈 aparece solo al pasar el mouse */
}

/* Colores alternos para diferenciar jerarquías */
div:nth-child(odd) {
  background-color: rgba(0, 123, 255, 0.05);
}
div:nth-child(even) {
  background-color: rgba(40, 167, 69, 0.05);
}
div:hover {
  background-color: rgba(255, 193, 7, 0.1);
  border-color: rgba(255, 193, 7, 0.6);
  transition: 0.3s;
}
div {
  border: 2px dashed #aaa;
  border-radius: 8px;
  margin: 8px;
  padding: 16px;
  box-shadow: 0 0 4px rgba(0,0,0,0.1);
  position: relative;
}
div::before {
  content: attr(class);
  position: absolute;
  top: -10px;
  left: 10px;
  background: white;
  color: #555;
  font-size: 11px;
  padding: 2px 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
div {
  --depth: 0;
  background: hsl(calc(var(--depth) * 40), 70%, 95%);
  border: 1px solid #ddd;
  padding: 10px;
  margin: 5px;
  border-radius: 5px;
}

/* Cada nivel más profundo cambia el color */
div div { --depth: 1; }
div div div { --depth: 2; }
div div div div { --depth: 3; }
div div div div div { --depth: 4; }
</style>

