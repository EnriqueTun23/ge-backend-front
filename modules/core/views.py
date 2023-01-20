""" Views core login and api """
# Django
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.views import View
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import update_session_auth_hash, login, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
# Utils
from modules.utils.mixins import AuthMixin
# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, parsers, renderers
# Django-rest-passwordreset
from django_rest_passwordreset.signals import reset_password_token_created

# Serializers
from .serializers import LoginSerializer, CustomTokenSerializer
# from modules.users.serializers import LoginModelSerializer
# Forms
from .forms import PasswordResetForm
# models 
from modules.users import models
# token
from modules.users.token import account_activation_token
""" ---------------- Class Authentication UI ----------------------"""
User_login = get_user_model()


class Login(LoginView):
    """ Login """
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        usuario = self.request.user
        if usuario.is_anonymous:
            return super(Login, self).dispatch(request, *args, **kwargs)
        else:
            return redirect('home')


class LoginError(LoginView):
    """ Login Review """
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        #obtengo el contexto actual
        context=super(LoginError, self).get_context_data(**kwargs)
         # recojo el parametro 
        parametro = self.kwargs.get('pk', None) 
         #agrego parametro al diccionario de contexto
        context['parametro'] = parametro            
        return context



class Logout(LogoutView):
    """ Logout """
    pass

"""------------ password reset --------------------------"""
class ResetPassword(PasswordResetView):
    email_template_name = 'password/template_email.html'
    html_email_template_name = 'password/template_email.html'
    subject_template_name = 'password/password_reset_subject.txt'
    success_url = reverse_lazy('reset_password_done')
    template_name = 'password/template_reset_password.html'
    
class ResetPasswordDone(PasswordResetDoneView):
    template_name = 'password/template_password_done.html'

class ResetPasswordConfirm(PasswordResetConfirmView):
    template_name = 'password/template_reset_confirm.html'
    success_url = reverse_lazy('login_check', kwargs={'pk': 1})


class ResetPasswordComplete(PasswordResetCompleteView):
    template_name = 'password/template_reset_complete.html'

""" ----------------------------------------------------------"""

class Activate(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            usuario = models.User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, usuario.DoesNotExist):
            usuario = None
        
        if usuario is not None and account_activation_token.check_token(usuario, token):
            usuario.is_verified = True
            usuario.save()
            return redirect('validateSelect')
        else:
            return redirect('errorValidate')

""" ------- Index ------- """

class AdministrativeView(AuthMixin, TemplateView):
# class AdministrativeView(TemplateView):
    """ administrative panel"""
    template_name = 'users/administrador/admin_index.html'
    redirect_field_name = 'home'


""" ------- validation email url ------- """
class SendEmailToken(TemplateView):
    template_name = 'validation/seed.html'


class ValidateSelectView(TemplateView):
    template_name = 'validation/select.html'


class ErrorValidate(TemplateView):
    template_name =  'validation/error.html'

"""---------------------------------------"""


""" ------------------- Class Authentication API -------------------------- """

# class LoginApiView(APIView):
#     """ Login API View """
#     def post(self, request, *args, **kwargs):
#         """ Post method manager """
#         serializer = LoginSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         login = serializer.save()
#         data = {
#             'user': LoginModelSerializer(login).data
#         }
#         return Response(data=data, status=status.HTTP_200_OK)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()

""" --------------------------------------------------- """