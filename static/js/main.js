function changeLanguage() {
  const languagesList = document.getElementById("languages");
  if (languagesList.style.display === "none") {
    languagesList.style.display = "block";
  } else {
    languagesList.style.display = "none";
  }
} 