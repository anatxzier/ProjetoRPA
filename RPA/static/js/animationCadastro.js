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

const togglePassword = document.querySelector('#togglePassword');
const passwordField = document.querySelector('#id_passwordCadastro');

togglePassword.addEventListener('click', function () {
    // Verifica o tipo atual do campo de senha
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    // Altera o tipo de password para text e vice-versa
    passwordField.setAttribute('type', type);

    // Altera o ícone entre "visibility" e "visibility_off"
    this.textContent = type === 'password' ? 'visibility_off' : 'visibility';
});
