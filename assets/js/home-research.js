// Load each PDF only after the reader is opened.
document.querySelectorAll(".paper-reader").forEach((reader) => {
  reader.addEventListener("toggle", () => {
    if (!reader.open || reader.querySelector("iframe")) return;
    const frame = document.createElement("iframe");
    frame.src = reader.dataset.pdf;
    frame.title = reader.closest("article").querySelector("h3").textContent.trim() + " — PDF";
    frame.loading = "lazy";
    reader.querySelector(".paper-pdf").append(frame);
  });
});
