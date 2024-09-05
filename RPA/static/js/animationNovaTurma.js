
    // Obter os elementos necessários
    var modal = document.getElementById("myModal");
    var btn = document.getElementById("buttonModal");
    var span = document.getElementsByClassName("close")[0];
    var button = document.getElementsByClassName("voltar")[0];

    // Quando o botão for clicado, mostra a modal
    btn.onclick = function(event) {
        event.preventDefault(); // Previne o envio do formulário
        modal.style.display = "block";
    }

    // Quando o usuário clicar no "x", esconde a modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Quando clicar em "voltar" a modal fecha
    button.onclick = function(){
        modal.style.display = "none";
    }

    // Quando o usuário clicar fora da modal, esconde a modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    document.addEventListener('DOMContentLoaded', function () {
        const inputFile = document.getElementById('arquivos');
        const fileNameDisplay = document.getElementById('file-name');

        inputFile.addEventListener('change', function(event) {
            if (event.target.files.length > 0) {
                const fileName = event.target.files[0].name;
                fileNameDisplay.textContent = `Arquivo selecionado: ${fileName}`;
            } else {
                fileNameDisplay.textContent = 'Nenhum arquivo selecionado';
            }
        });
    });

