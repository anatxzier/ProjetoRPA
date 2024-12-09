// Espera o conteúdo da página ser totalmente carregado
document.addEventListener('DOMContentLoaded', function() {
    // Obtém o contêiner de mensagem de sucesso e erro, caso existam
    const successMessages = document.getElementById('alert-containerCadastro-success');
    const errorMessage = document.getElementById('alert-containerCadastro-error');
    
    // Se houver uma mensagem de sucesso, exibe o alerta de sucesso
    if (successMessages) {
        swal("", "Usuário cadastrado com sucesso!", "success");
    }
    // Se houver uma mensagem de erro, exibe o alerta de erro
    if (errorMessage) {
        swal("", "Erro ao cadastrar usuário!", "error");
    }
});

// Obtém os elementos necessários para alternar a visibilidade da senha
const togglePassword = document.querySelector('#togglePassword');
const passwordField = document.querySelector('#id_passwordCadastro');

// Adiciona um evento de clique ao botão de alternância da visibilidade da senha
togglePassword.addEventListener('click', function () {
    // Verifica o tipo atual do campo de senha ('password' ou 'text')
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    // Altera o tipo do campo de senha entre 'password' e 'text'
    passwordField.setAttribute('type', type);

    // Altera o ícone de visibilidade da senha entre 'visibility' e 'visibility_off'
    this.textContent = type === 'password' ? 'visibility_off' : 'visibility';
});
