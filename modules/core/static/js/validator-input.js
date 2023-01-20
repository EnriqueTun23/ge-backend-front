
function validatorEmail() {
    var email = $('#email-login').val();
    if(validateEmail(email)) return $('#error-email').text('')
    return $('#error-email').text('El email esta mal')
}
function validatorEmailReset() {
    var email = $('#id_email').val();
    if(validateEmailReset(email)) return $('#error-email').text('')
    return $('#error-email').text('El email esta mal')
}

function validateEmail(email){
    var emailReg = new RegExp(/^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/i);
    return emailReg.test(email);
}
function validateEmailReset(email){
    var emailReg = new RegExp(/^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])/i);
    return emailReg.test(email);
}

$('#check-password').click( function() {
    if($(this).hasClass('fa-eye')){
        $('#password-field').attr('type', 'text');
        $('#check-password').addClass('fa-eye-slash').removeClass('fa-eye');
    }else {
        $('#password-field').attr('type','password');
        $('#check-password').addClass('fa-eye').removeClass('fa-eye-slash');
    }
})



$("#login").click(function(event){
    event.preventDefault();
    // $.removeCookie('tokens_pk');
    iniciar_sesion();
});

function iniciar_sesion() {
    $('#login_form').submit()
    // var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    // var form = $('#login_form').closest('form')
    // $.ajax({
    //     type: 'POST',
    //     data: form.serialize(),
    //     url: 'ge/login/',
    //     dataType: 'json',
        
    // }).done(function(data) {
    //     $.cookie('tokens_access', data.access, { expires: 1 });
    //     $.cookie('tokens_refresh', data.refresh, { expires: 1 })
    // }).fail(function(fail) {
    //     $('.error-global').show()
    // })
    
    // $.ajax({
    //     type: 'POST',
    //     data: form.serialize(),
    //     url: ,
    //     dataType: 'json'
    // }).done(function(data){
    //     $.cookie('tokens_access', data.access, { expires: 1 });
    //     $.cookie('tokens_refresh', data.refresh, { expires: 1 });
    //     $.ajax({
    //         type: 'POST',
    //         data: form.serialize(),
    //         url: url_redirect_login,
    //         dataType: 'json'
    //     }).done(function(login){
    //         $.cookie('tokens_pk', login.user.pk, { expires: 1 });
    //         window.location.href = url_redirect;
    //     }).fail(function(error) {
    //         console.log(error)
    //     })
    // }).fail(function(fail) {
    //     $('.error-global').show()
    // })
}