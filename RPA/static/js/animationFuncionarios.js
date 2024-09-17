function toggleDetails(contentId, arrowId) {
    var content = document.getElementById(contentId);
    var arrow = document.getElementById(arrowId);

    // Verifique o estado atual de exibição do conteúdo e altere-o corretamente
    if (content.style.display === "none" || content.style.display === "") {
        content.style.display = "block";
        arrow.textContent = "▲"; // Muda a seta para cima
    } else {
        content.style.display = "none";
        arrow.textContent = "▼"; // Muda a seta para baixo
    }
}
