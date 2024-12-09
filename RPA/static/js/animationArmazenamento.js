
function openModal(modalId) {
    // Obtém o modal pelo ID fornecido
    var modal = document.getElementById(modalId);
    if (modal) {
        // Se o modal existir, exibe ele definindo o display como 'block'
        modal.style.display = 'block';
    }
  }
  
  function closeModal(modalId) {
    // Obtém o modal pelo ID fornecido
    var modal = document.getElementById(modalId);
    if (modal) {
        // Se o modal existir, oculta ele definindo o display como 'none'
        modal.style.display = 'none';
    }
  }
  
  // Fechar o modal ao clicar fora dele
  window.onclick = function(event) {
    // Verifica se o clique foi fora do conteúdo do modal (clicando na área de fundo)
    if (event.target.classList.contains('modal')) {
        // Se o clique foi fora, chama a função closeModal passando o ID do modal (event.target.id)
        closeModal(event.target.id);
    }
  }
