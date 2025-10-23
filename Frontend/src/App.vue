<template>
  <div class="d-flex">
    <SidebarMenu />

    <div class="main-layout flex-grow-1 d-flex flex-column min-vh-100">
      <!-- <Header /> -->

      <main class="flex-grow-1 p-3">
        <RouterView />
      </main>

      <!-- <Footer /> -->
    </div>
  </div>
</template>

<script setup>
import { RouterView } from "vue-router";
import SidebarMenu from "./components/desing/organisms/sidebarMenu.vue";
</script>
<style scoped>
.main-layout {
  transition: padding-left 0.3s ease;
  padding-left: 220px; /* cuando sidebar expandido */
}

.sidebar.collapsed ~ .main-layout {
  padding-left: 70px; /* cuando sidebar colapsado */
}
.btn-primary {
  background-color: var(--color-primary) !important;
  border-color: var(--color-primary) !important;
}

.btn-primary:hover {
  background-color: var(--color-primary) !important;
  opacity: 0.85;
}
.text-primary {
  color: var(--bs-primary) !important;
}
.icon-primary {
  color: var(--bs-primary);
}
</style>
