document.addEventListener('DOMContentLoaded', function() {
    const successMessages = document.getElementById('alert-containerCadastro-success');
    const errorMessage = document.getElementById('alert-containerCadastro-error');

    if (successMessages) {
        swal("", "Usuário cadastrado com sucesso!", "success");
    }

    if (errorMessage) {
        swal("", "Erro ao cadastrar usuário!", "error");
    }
});

