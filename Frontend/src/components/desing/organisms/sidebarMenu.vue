<template>
  <div>
    <!-- Sidebar -->
    <div
      :class="[
        'sidebar position-fixed vh-100 d-flex flex-column p-3 transition-all shadow',
        isCollapsed ? 'collapsed' : 'expanded',
      ]"
    >
      <!-- Botón toggle -->
      <div class="d-flex justify-content-end">
        <button
          class="btn btn-light btn-sm rounded-circle shadow-sm toggle-btn"
          type="button"
          @click="toggleSidebar"
        >
          <i
            :class="
              isCollapsed
                ? 'bi bi-chevron-right text-success'
                : 'bi bi-chevron-left text-success'
            "
          ></i>
        </button>
      </div>

      <!-- Logo -->
      <div class="mb-4 text-center" v-if="!isCollapsed">
        <img
          src="@/assets/circle.png"
          style="width: 60px"
          class="mx-auto d-block"
          alt="Logo"
        />
      </div>

      <!-- Menú principal -->
      <ul class="navbar-nav flex-column gap-2">
        <li class="nav-item">
          <router-link
            class="nav-link d-flex align-items-center"
            active-class="active-link"
            :to="{ name: 'form-forms' }"
          >
            <i class="bi bi-person"></i>
            <span v-if="!isCollapsed" class="ms-2">Formulario</span>
          </router-link>
        </li>
      </ul>

      <hr class="my-3 w-100 text-white opacity-50" v-if="!isCollapsed" />


    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const isCollapsed = ref(false);

const toggleSidebar = () => {
  isCollapsed.value = !isCollapsed.value;
};
</script>

<style scoped>
.sidebar {
  z-index: 1000;
  background: linear-gradient(180deg, #198754, #145c32);
  color: white;
  border-radius: 0 15px 15px 0;
}

.sidebar .nav-link {
  color: rgba(255, 255, 255, 0.85);
  padding: 10px 12px;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.sidebar .nav-link i {
  font-size: 1.2rem;
}

/* Hover en links */
.sidebar .nav-link:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

/* Link activo */
.sidebar .active-link {
  background: #0d683a;
  color: #fff;
  font-weight: 600;
}

.sidebar .active-link i {
  color: #fff !important;
}

.expanded {
  width: 220px;
}

.collapsed {
  width: 70px;
}

.transition-all {
  transition: width 0.3s ease;
}


.collapsed .nav-link {
  width: 45px;
  height: 45px;
  border-radius: 50% !important;
  background: #198754;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.collapsed .nav-link i {
  color: #fff;
  font-size: 1.3rem;
}


.collapsed .nav-link:hover {
  background: #0d683a;
  color: #fff;
}

/* Botón toggle flotante */
.toggle-btn {
  background: #fff;
  border: none;
}
</style>
