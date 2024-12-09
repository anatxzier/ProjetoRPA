// Adiciona um ouvinte de evento para o evento "beforeunload" (antes da página ser descarregada)
window.addEventListener("beforeunload", function() {
    // Reseta o formulário com o ID "FormsCadastro" antes da página ser descarregada
    document.getElementById("FormsCadastro").reset();
});

