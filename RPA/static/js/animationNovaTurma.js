// Obter os elementos necessários
var modal = document.getElementById("myModal");
var btn = document.getElementById("buttonModal");
var span = document.getElementsByClassName("close")[0];
var buttonVoltarNova = document.getElementsByClassName("nao")[0];
var buttonSub = document.getElementsByClassName("sim")[0];
var formulario = document.getElementById("formNova");
var userChoiceInput = document.getElementById("userChoice");

// Quando o botão "Iniciar" for clicado, exibe a modal
btn.onclick = function(event) {
    event.preventDefault(); // Previne o envio imediato do formulário
    modal.style.display = "block";
}

// Fecha a modal ao clicar no "x"
span.onclick = function() {
    modal.style.display = "none";
}

// Fecha a modal ao clicar fora dela
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Atualiza o valor do campo oculto e envia o formulário quando "Sim" for clicado
buttonSub.onclick = function() {
    userChoiceInput.value = "sim"; // Define o valor como "sim"
    formulario.submit(); 
}

// Atualiza o valor do campo oculto e envia o formulário quando "Não" for clicado
buttonVoltarNova.onclick = function() {
    modal.style.display = "none"; // Fecha o modal
    userChoiceInput.value = "não"; // Define o valor como "não"
    formulario.submit(); // Envia o formulário
}

// Exibe mensagens de sucesso ou erro
document.addEventListener('DOMContentLoaded', function() {
    const successMessages = document.getElementById('alert-containerNovaTurma-success');
    const errorMessage = document.getElementById('alert-containerNovaTurma-error');

    if (successMessages) {
        swal("", "O registro iniciou!", "success");
    }

    if (errorMessage) {
        swal("", "Erro ao cadastrar usuário!", "error");
    }

    const inputFile = document.getElementById('file-upload');
    const fileNameDisplay = document.getElementById('file-names');

    // Limitar a seleção para um único arquivo
    inputFile.addEventListener('change', function(event) {
        if (event.target.files.length > 0) {
            const fileName = event.target.files[0].name;
            fileNameDisplay.textContent = `Arquivo selecionado: ${fileName}`;
        } else {
            fileNameDisplay.textContent = 'Nenhum arquivo selecionado';
        }
    });

    // Exibe mensagem de erro se necessário
    if (errorMessage) {
        swal("", "Ocorreu um erro durante o processamento do formulário!", "error");
    }
});