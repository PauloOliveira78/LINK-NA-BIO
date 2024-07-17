function toggleTheme() {
  const root = document.documentElement
  const toggleContainer = document.getElementById("theme-toggle-container")

  root.classList.toggle("light")

  if (root.classList.contains("light")) {
    toggleContainer.classList.add("light")
  } else {
    toggleContainer.classList.remove("light")
  }
}

document.getElementById("theme-toggle").addEventListener("click", toggleTheme)
