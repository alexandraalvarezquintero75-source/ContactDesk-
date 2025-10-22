import { createApp } from 'vue'
import App from './App.vue'
import 'primeicons/primeicons.css'

// Estilos globales
// import '@/assets/styles/_base.scss'

// PrimeVue
import PrimeVue from 'primevue/config'
import Button from 'primevue/button'



// Crear instancia
const app = createApp(App)

app.use(PrimeVue)
// Componentes PrimeVue
app.component('Button', Button)
// Montar app
app.mount('#app')
