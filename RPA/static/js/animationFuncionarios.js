function toggleDetails(contentId, arrowId) {
    var content = document.getElementById(contentId);
    var arrow = document.getElementById(arrowId);

    console.log('Toggling:', contentId, arrowId);
    console.log('Content:', content);
    console.log('Arrow:', arrow);

    // Em vez de verificar o estilo diretamente, podemos usar getComputedStyle para obter o valor atual
    var isHidden = window.getComputedStyle(content).display === "none";

    if (isHidden) {
        // Se estiver escondido, mostra o conteúdo
        content.style.display = "block";
        arrow.textContent = "▲"; 
    } else {
        // Se estiver visível, esconde o conteúdo
        content.style.display = "none";
        arrow.textContent = "▼"; 
    }
}
