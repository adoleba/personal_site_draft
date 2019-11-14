function changeLanguage() {
  const languagesList = document.getElementById("languages");
  if (languagesList.style.display === "none") {
    languagesList.style.display = "block";
  } else {
    languagesList.style.display = "none";
  }
  setTimeout(function() {
    languagesList.style.display = "none";
    }, 3000);
}
