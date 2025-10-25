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

