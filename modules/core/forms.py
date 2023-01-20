""" Form validation password reset"""
import unicodedata
from base64 import b64encode
from mimetypes import guess_type
# Django
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.staticfiles import finders



UserModel = get_user_model()

def convertir_base64():
    with open(finders.find('img/LogotipoGE.png'), 'rb') as f:
        logo =  f.read()
    
    codificar = b64encode(logo)
    content_type, encoding = guess_type('img/LogotipoGE.png')

    return "data:%s;base64,%s" % (content_type, codificar)


def _unicode_ci_compare(s1, s2):
    """
    Perform case-insensitive comparison of two identifiers, using the
    recommended algorithm from Unicode Technical Report 36, section
    2.11.2(B)(2).
    """
    return unicodedata.normalize('NFKC', s1).casefold() == unicodedata.normalize('NFKC', s2).casefold()

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        """
        Envíe un  django.core.mail.EmailMultiAlternatives a `to_email`(esta parte hace el envio del email).
        """
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')

        email_message.send()

    def get_users(self, email):
        """Dado un correo electrónico, devuelve los usuarios coincidentes que deberían recibir un reinicio.
        Esto permite que las subclases personalicen más fácilmente las políticas predeterminadas.
        que evitan usuarios inactivos y usuarios con contraseñas inutilizables de
        restableciendo su contraseña.
        """
        email_field_name = UserModel.get_email_field_name()
        active_users = UserModel._default_manager.filter(**{
            '%s__iexact' % email_field_name: email,
            'is_active': True,
        })
        return (
            u for u in active_users
            if u.has_usable_password() and
            _unicode_ci_compare(email, getattr(u, email_field_name))
        )

    def save(self, domain_override=None,
             subject_template_name='password/password_reset_subject.txt',
             email_template_name='password/template_email.html',
             use_https=False, 
             token_generator= default_token_generator,
             from_email=None, 
             request=None, 
             html_email_template_name='password/template_email.html',
             extra_email_context=None):
        """
        Genere un enlace de un solo uso para restablecer la contraseña y envíelo al usuario.
        """
        email = self.cleaned_data["email"]
        if not domain_override:
            current_site = get_current_site(request)
            site_name = current_site.name
            domain = current_site.domain
        else:
            site_name = domain = domain_override
        email_field_name = UserModel.get_email_field_name()
        for user in self.get_users(email):
            user_email = getattr(user, email_field_name)
            context = {
                'email': user_email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'user': user,
                'token': token_generator.make_token(user),
                #'logo': "<img src="{% static 'img/LogotipoGE.png' %}">",
                'protocol': 'https' if use_https else 'http',
                **(extra_email_context or {}),
            }
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                user_email, html_email_template_name=html_email_template_name,
            )
