function changeLanguage() {
  const languagesList = document.getElementById("languages");
  if (window.innerWidth > 268) {
      if (languagesList.style.display === "none") {
          languagesList.style.display = "block";
      }
  }
}

function changeLanguageOut() {
  const languagesList = document.getElementById("languages");
  if (window.innerWidth > 268) {
      if (languagesList.style.display === "block") {
          languagesList.style.display = "none";
      }
  }
}

