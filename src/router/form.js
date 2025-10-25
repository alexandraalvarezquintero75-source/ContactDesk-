import indexViewForm from '@/views/form/indexViewForm.vue'
import Form from '@/views/form/components/Form.vue'

export default [
  {
    path: '/forms',
    name: 'forms',
    component: indexViewForm
  },
  {
    path: '/form-forms',
    name: 'form-forms',
    component: Form
  }
]