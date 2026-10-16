document.addEventListener("DOMContentLoaded", () => {
  const search = document.getElementById("tableSearch");
  const table = document.getElementById("productsTable");
  if (search && table) {
    search.addEventListener("input", () => {
      const term = search.value.toLocaleLowerCase("pt-BR");
      table.querySelectorAll("tbody tr").forEach(row => {
        row.style.display = row.innerText.toLocaleLowerCase("pt-BR").includes(term) ? "" : "none";
      });
    });
  }
  document.querySelectorAll(".flash").forEach(item => {
    setTimeout(() => item.classList.add("fade-out"), 4000);
  });
});
