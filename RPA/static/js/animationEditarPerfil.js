// Seleciona os elementos do DOM
const btnEditar = document.getElementById("submitButton")[0];  // Botão de "Confirmar" na modal
const formEditar = document.getElementById("formEditar");  // Formulário principal
const btnModal = document.querySelector(".btn-editar2");  // Botão de "Confirmar Alterações"
var modal = document.getElementById("myModal2");  // A modal
var span = document.getElementsByClassName("close")[0];  // Botão de fechar da modal
var buttonVoltar = document.getElementsByClassName("voltar")[0];  // Botão "Voltar"


document.addEventListener('DOMContentLoaded', function() {
    // Verifica se a modal deve estar aberta com base no atributo "data-modal-open"
    const modalOpenFlag = document.getElementById('modal-open-flag').getAttribute('data-modal-open');

    if (modalOpenFlag === "true") {
        // Abre a modal assim que a página carrega
        document.getElementById("myModal2").style.display = "block";
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
        document.getElementById("formEditar").submit();  // Submete o formulário
    }
});

