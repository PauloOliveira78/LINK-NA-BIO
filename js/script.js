function toggleTheme() {
  const root = document.documentElement;
  const toggleContainer = document.getElementById("theme-toggle-container");

  if (root) {
    root.classList.toggle("light");
  }

  if (toggleContainer) {
    if (root.classList.contains("light")) {
      toggleContainer.classList.add("light");
    } else {
      toggleContainer.classList.remove("light");
    }
  }
}

// Verifica o estado do tema ao carregar a página
function initializeTheme() {
  const root = document.documentElement;
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme) {
    root.classList.toggle("light", savedTheme === "light");
    const toggleContainer = document.getElementById("theme-toggle-container");
    if (toggleContainer) {
      toggleContainer.classList.toggle("light", savedTheme === "light");
    }
  }
}

// Define o tema ao clicar no botão
document.getElementById("theme-toggle").addEventListener("click", () => {
  toggleTheme();
  // Armazena o estado do tema no localStorage
  const root = document.documentElement;
  localStorage.setItem("theme", root.classList.contains("light") ? "light" : "dark");
});

// Inicializa o tema ao carregar a página
initializeTheme();
