// Obter os elementos necessários
var modal = document.getElementById("myModal");
var btn = document.getElementById("buttonModal");
var span = document.getElementsByClassName("close")[0];
var buttonVoltar = document.getElementsByClassName("voltar")[0];
var buttonSub = document.getElementsByClassName("iniciar")[0];
var formulario = document.getElementById("formNova");


document.addEventListener('DOMContentLoaded', function() {
    const successMessages = document.getElementById('alert-containerNovaTurma-success');
    const errorMessage = document.getElementById('alert-containerNovaTurma-error');

    if (successMessages) {
        swal("", "O registro iniciou!", "success");
    }

    if (errorMessage) {
        swal("", "Erro ao cadastrar usuário!", "error");
    }
});

// Quando o botão "Iniciar" for clicado, exibe a modal
btn.onclick = function(event) {
    event.preventDefault(); // Previne o envio imediato do formulário
    modal.style.display = "block";
}

// Fecha a modal ao clicar no "x"
span.onclick = function() {
    modal.style.display = "none";
}

// Fecha a modal ao clicar no botão "Voltar"
buttonVoltar.onclick = function() {
    modal.style.display = "none";
}

// Fecha a modal ao clicar fora dela
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


buttonSub.onclick = function() {
    formulario.submit(); 
}
//////////////////////////////////////////////////////////////////////////////

document.addEventListener('DOMContentLoaded', function () {
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
});

