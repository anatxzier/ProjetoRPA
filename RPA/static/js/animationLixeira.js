// Obter os elementos necessários
var modalDelete = document.getElementById("modalDelete");
var btnDelete = document.getElementById("buttonModalDelete");
var modalRestore = document.getElementById("modalRestore");
var btnRestore = document.getElementById("buttonModalRestore");

var spanClose = document.getElementsByClassName("closeDeleteRestore");
var buttonClose = document.getElementsByClassName("voltarDeleteRestore");

// Quando o botão de deletar for clicado, mostra a modal de deletar
btnDelete.onclick = function(event) {
    event.preventDefault(); // Previne o envio do formulário
    modalDelete.style.display = "block";
}

// Quando o botão de restaurar for clicado, mostra a modal de restaurar
btnRestore.onclick = function(event) {
    event.preventDefault(); // Previne o envio do formulário
    modalRestore.style.display = "block";
}

// Quando o usuário clicar no "x" da modal de deletar ou restaurar, esconde a modal
for (let i = 0; i < spanClose.length; i++) {
    spanClose[i].onclick = function() {
        modalDelete.style.display = "none";
        modalRestore.style.display = "none";
    }
}

// Quando clicar em "voltar" nas modais, elas fecham
for (let i = 0; i < buttonClose.length; i++) {
    buttonClose[i].onclick = function() {
        modalDelete.style.display = "none";
        modalRestore.style.display = "none";
    }
}

// Quando o usuário clicar fora da modal, esconde a modal
window.onclick = function(event) {
    if (event.target == modalDelete) {
        modalDelete.style.display = "none";
    }
    if (event.target == modalRestore) {
        modalRestore.style.display = "none";
    }
}
