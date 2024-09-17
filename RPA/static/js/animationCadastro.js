setTimeout(function () {
    var successAlert = document.getElementById('alert-success-container');
    var errorAlert = document.getElementById('alert-error-container');
    if (successAlert) {
        successAlert.style.display = 'none';
    }
    if (errorAlert) {
        errorAlert.style.display = 'none';
    }
}, 2500);