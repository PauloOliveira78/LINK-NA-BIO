document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("my-form")
  const confirmationMessage = document.getElementById("confirmationMessage")

  form.addEventListener("submit", function (event) {
    event.preventDefault() // Previne o comportamento padrão de envio do formulário

    // Enviar e-mail usando EmailJS
    emailjs.sendForm("service_pugbk7d", "template_dfgofgx", form).then(
      function (response) {
        console.log("Success:", response)

        // Exibir mensagem de confirmação
        confirmationMessage.classList.add("show")

        // Ocultar mensagem de confirmação após 5 segundos
        setTimeout(function () {
          confirmationMessage.classList.remove("show")
        }, 5000) // 5000 milissegundos = 5 segundos

        // Limpar o formulário após o envio
        form.reset()
      },
      function (error) {
        console.error("Error:", error)
      }
    )
  })
})
