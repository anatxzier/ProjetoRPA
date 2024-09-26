setTimeout(function () {
    var alertContainer = document.getElementById('alert-containerLogin');
    if (alertContainer) {
        alertContainer.style.display = 'none';
    }
}, 2500);

const togglePasswordLogin = document.querySelector('#togglePasswordLogin');
const passwordFieldLogin = document.querySelector('#id_passwordLogin');

togglePasswordLogin.addEventListener('click', function () {
    // Verifica o tipo atual do campo de senha
    const type = passwordFieldLogin.getAttribute('type') === 'password' ? 'text' : 'password';
    // Altera o tipo de password para text e vice-versa
    passwordFieldLogin.setAttribute('type', type);

    // Altera o ícone entre "visibility" e "visibility_off"
    this.textContent = type === 'password' ? 'visibility_off' : 'visibility';
});
