import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap-icons/font/bootstrap-icons.css'
import router from './router/routes'
// import tooltip from './directives/tooltip'
// import themeState from './stores/theme-state'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
import { BootstrapVue3 } from 'bootstrap-vue-3'
// import tooltip from './directives/tooltip'
// import PrimeVue from 'primevue/config'
// import '@primevue/themes/lara'

// import 'primeicons/primeicons.css'


const app = createApp(App)
// app.directive('tooltip', tooltip)
// app.use(router)
// app.use(instanceI18n)
app.use(BootstrapVue3)
app.use(router)
// app.use(themeState)
// app.use(PrimeVue)
app.mount('#app')
