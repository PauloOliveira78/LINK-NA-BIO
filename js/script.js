document.addEventListener("DOMContentLoaded", function () {
  const themeToggleButton = document.getElementById("theme-toggle")
  const body = document.body

  // Função para definir a classe do dispositivo
  function setDeviceClass() {
    if (window.innerWidth <= 768) {
      body.classList.add("mobile")
      body.classList.remove("desktop")
    } else {
      body.classList.add("desktop")
      body.classList.remove("mobile")
    }
  }

  // Definir a classe do dispositivo ao carregar a página
  setDeviceClass()

  // Atualizar a classe do dispositivo ao redimensionar a janela
  window.addEventListener("resize", setDeviceClass)

  themeToggleButton.addEventListener("click", function () {
    if (body.classList.contains("root")) {
      body.classList.remove("root")
      body.classList.add("light")
    } else {
      body.classList.remove("light")
      body.classList.add("root")
    }
  })
})
