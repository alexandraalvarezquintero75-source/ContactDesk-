// import { createRouter, createWebHistory } from 'vue-router'
// import Home from '@/views/home/home.vue'
// import { APP_ROUTE_NAMES } from '@/constants/routeNames'
// import PetForm from '@/views/pets/components/PetForm.vue'
// import indexViewPets from '@/views/pets/indexViewPets.vue'
// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
// { path: '/', name: APP_ROUTE_NAMES.HOME, component: Home },
  

//  { path: '/pets', name: APP_ROUTE_NAMES.PETS, component: indexViewPets },
//  { path: '/form-pets', name: APP_ROUTE_NAMES. FORM_PETS, component: PetForm },
//   ],
// })
// // DEBUG: muestra en consola las rutas registradas (borra luego esto)
// console.log('ROUTER REGISTERED ROUTES:', router.getRoutes().map(r => ({ name: r.name, path: r.path })))
// window.__router = router // te da acceso desde consola del navegador para inspeccionar si lo necesitas

// export default router

import { createRouter, createWebHistory } from 'vue-router'

// Importar rutas por módulo
import homeRoutes from './home.js'
import FormRoutes from './form.js'

// Combinar todas las rutas en un solo array
const routes = [
  ...homeRoutes,
  ...FormRoutes
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// DEBUG: muestra las rutas registradas
console.log('ROUTER REGISTERED ROUTES:', router.getRoutes().map(r => ({ name: r.name, path: r.path })))
window.__router = router

export default router

