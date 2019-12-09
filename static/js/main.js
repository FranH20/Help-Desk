$('#ticket').on('submit', function(e) {
    var form = this;
    e.preventDefault();
const swalWithBootstrapButtons = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

swalWithBootstrapButtons.fire({
  title: 'Estas seguro?',
  text: "Aún puedes revertir esto!",
  type: 'Cuidado',
  showCancelButton: true,
  confirmButtonText: 'Si, Enviar!',
  cancelButtonText: 'No, Cancelar!',
  reverseButtons: true,
     backdrop: `
    rgba(0,0,123,0.4)
    url("http://giphygifs.s3.amazonaws.com/media/sIIhZliB2McAo/giphy.gif")
    center left
    no-repeat
  `
}).then((result) => {
  if (result.value) {
    swalWithBootstrapButtons.fire(
      'Enviado!',
      'El ticket fue enviado.',
      'Con exito!'
    )
      form.submit();
  } else if (
    /* Read more about handling dismissals below */
    result.dismiss === Swal.DismissReason.cancel
  ) {
    swalWithBootstrapButtons.fire(
      'Cancelado',
      'Tu ticket imaginario esta a salvo :)',
      'error'
    )
  }
})
});