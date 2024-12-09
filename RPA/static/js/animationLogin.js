// Define um temporizador para esconder a mensagem de alerta após 2.5 segundos
setTimeout(function () {
    var alertContainer = document.getElementById('alert-containerLogin');
    if (alertContainer) {
        alertContainer.style.display = 'none';
    }
}, 2500); // Tempo de espera de 2.5 segundos (2500 milissegundos)

// Seleciona o botão de mostrar/esconder senha e o campo de senha do login
const togglePasswordLogin = document.querySelector('#togglePasswordLogin');
const passwordFieldLogin = document.querySelector('#id_passwordLogin');

// Adiciona um evento de clique ao botão de mostrar/esconder senha
togglePasswordLogin.addEventListener('click', function () {
    // Verifica o tipo atual do campo de senha
    const type = passwordFieldLogin.getAttribute('type') === 'password' ? 'text' : 'password';
    // Altera o tipo de password para text e vice-versa
    passwordFieldLogin.setAttribute('type', type);

    // Altera o ícone entre "visibility" e "visibility_off"
    this.textContent = type === 'password' ? 'visibility_off' : 'visibility';
});
