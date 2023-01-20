if ($(".errorlist").length == 0) {
    $("#exclamation-hidden").hide();
} else {
    $("#exclamation-hidden").show();
}
$('#check-password1').click(function () {
    if ($(this).hasClass('fa-eye')) {
        $('#id_new_password1').attr('type', 'text');
        $('#check-password1').addClass('fa-eye-slash').removeClass('fa-eye');
    } else {
        $('#id_new_password1').attr('type', 'password');
        $('#check-password1').addClass('fa-eye').removeClass('fa-eye-slash');
    }
})
$('#check-password2').click(function () {
    if ($(this).hasClass('fa-eye')) {
        $('#id_new_password2').attr('type', 'text');
        $('#check-password2').addClass('fa-eye-slash').removeClass('fa-eye');
    } else {
        $('#id_new_password2').attr('type', 'password');
        $('#check-password2').addClass('fa-eye').removeClass('fa-eye-slash');
    }
})

function validationPassword() {
    var password1 = $('#id_new_password1').val();
    if(validatePassword(password1)) return $('#error-password').text('')
    return $('#error-password').text('Por favor use 8 caracteres como mínimo')
}
function passwordVerific() {
    var password1 = $('#id_new_password1').val();
    var password2 = $('#id_new_password2').val();
    if (comparisonPassword(password1, password2)) return $('#error-password2').text('')
    return $('#error-password2').text('El password no es igual al de arriba')
}

function comparisonPassword(password1, password2) {
    if (password1 === password2) return true
    return false
}
function validatePassword(password) {
    if (password.length >= 8) return true
    return false
}