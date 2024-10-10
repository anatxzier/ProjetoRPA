function openModal(modalId) {
  var modal = document.getElementById(modalId);
  if (modal) {
      modal.style.display = 'block';
  }
}

function closeModal(modalId) {
  var modal = document.getElementById(modalId);
  if (modal) {
      modal.style.display = 'none';
  }
}

// Fechar o modal ao clicar fora dele
window.onclick = function(event) {
  if (event.target.classList.contains('modal')) {
      closeModal(event.target.id);
  }
}
