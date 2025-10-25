<template>
  <form @submit.prevent>
    <div class="m-5">
      <!-- Fila 1 -->
      <div class="row mb-3">
        <div class="col-md-4">
          <input
            type="text"
            class="form-control"
            placeholder="Nombre"
            v-model="formUser.first_name"
          />
        </div>
        <div class="col-md-4">
          <input
            type="text"
            class="form-control"
            placeholder="Apellido"
            v-model="formUser.last_name"
          />
        </div>
        <div class="col-md-4">
          <input
            type="email"
            class="form-control"
            placeholder="Email"
            v-model="formUser.email"
          />
        </div>
      </div>

      <!-- Fila 2 -->
      <div class="row mb-3">
        <div class="col-md-4">
          <input
            type="text"
            class="form-control"
            placeholder="Teléfono"
            v-model="formUser.phone_number"
          />
        </div>
        <div class="col-md-4">
          <input
            type="password"
            class="form-control"
            placeholder="Contraseña"
            v-model="formUser.password"
          />
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 d-flex justify-content-center">
          <FormButtons />
        </div>
      </div>
    </div>
  </form>
</template>

<script setup>
import { ref } from "vue";
import FormButtons from "@/components/desing/atoms/FormButtons.vue";

const formUser = ref({
  first_name: "",
  last_name: "",
  email: "",
  phone_number: "",
  password: "",
});
</script>


