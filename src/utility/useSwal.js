import Swal from 'sweetalert2'

export function useSwal() {
  const showAlert = async (options) => {
    return await Swal.fire({
      ...options,
      customClass: {
        popup: 'rounded-4 shadow-lg',
        confirmButton: 'btn btn-success rounded-pill px-4 me-2', 
        cancelButton: 'btn btn-secondary rounded-pill px-4 ms-2', 
        icon: 'border-0'
      },
      buttonsStyling: false
    })
  }

  const showSuccess = async (message) => {
    return await showAlert({
      icon: 'success',
      text: message,
      position: 'top-end',
      timer: 1500,
      toast: true,
      showConfirmButton: false,
      customClass: {
        popup: 'rounded-pill bg-success text-white p-2 px-3 shadow-sm'
      }
    })
  }

  const showError = async (message) => {
    return await showAlert({
      icon: 'error',
      title: 'Error',
      text: message,
      position: 'top-end',
      timer: 1500,
      toast: true,
      showConfirmButton: false,
      customClass: {
        popup: 'rounded-pill bg-danger text-white p-2 px-3 shadow-sm'
      }
    })
  }

  const showConfirm = async (title, message, { iconColor = '#28a745' } = {}) => {
    return await showAlert({
      title,
      text: message,
      iconHtml: `<i class="bi bi-question-circle-fill" style="font-size:48px; color:${iconColor};"></i>`,
      showCancelButton: true,
      confirmButtonColor: iconColor,
      cancelButtonColor: '#6c757d',
      confirmButtonText: 'Sí',
      cancelButtonText: 'No',
      customClass: {
        popup: 'rounded-4 shadow-lg p-3',
        confirmButton: 'btn btn-success rounded-pill px-4 me-2',
        cancelButton: 'btn btn-secondary rounded-pill px-4 ms-2',
        icon: 'border-0'
      },
      buttonsStyling: false
    })
  }

  return { showSuccess, showError, showConfirm }
}
