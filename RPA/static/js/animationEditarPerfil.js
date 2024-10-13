// Seleciona os elementos do DOM
const btnEditar = document.getElementById("submitButton");  // Botão de "Confirmar" na modal
const formEditar = document.getElementById("formEditar");  // Formulário principal
const btnModal = document.querySelector(".btn-editar2");  // Botão de "Confirmar Alterações"
const modal = document.getElementById("myModal2");  // A modal
const span = document.getElementsByClassName("close")[0];  // Botão de fechar da modal
const buttonVoltar = document.getElementsByClassName("voltar")[0];  // Botão "Voltar"

// Abre a modal ao clicar em "Confirmar Alterações"
btnModal.onclick = function(event) {
    event.preventDefault();  // Previne o envio imediato do formulário
    modal.style.display = "block";  // Exibe a modal
}

// Fecha a modal ao clicar no "x"
span.onclick = function() {
    modal.style.display = "none";  // Fecha a modal
}

// Fecha a modal ao clicar fora dela
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";  // Fecha a modal se clicar fora
    }
}

// Fecha a modal ao clicar no botão "Voltar"
buttonVoltar.onclick = function() {
    modal.style.display = "none";  // Fecha a modal
}

// Quando o botão "Confirmar" da modal for clicado, submete o formulário
btnEditar.onclick = function() {
    formEditar.submit();  // Submete o formulário principal
}
