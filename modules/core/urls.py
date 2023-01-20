""" Urls core """

from django.urls import path, include
from .views import (
    Login, LoginError, Logout, 
    ResetPassword, ResetPasswordConfirm, ResetPasswordDone, ResetPasswordComplete, 
    AdministrativeView, Activate, SendEmailToken,
    ValidateSelectView, ErrorValidate)

urlpatterns = [
    # Authentication UI
    path('', AdministrativeView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('login/<int:pk>/', LoginError.as_view(), name='login_check'),
    path('logout/', Logout.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', Activate.as_view(), name='activate'),
    # Validate email
    path('envio/', SendEmailToken.as_view(), name='sendEmail'),
    path('validate/', ValidateSelectView.as_view(), name='validateSelect'),
    path('validate/error', ErrorValidate.as_view(), name='errorValidate'),
    # Reset Password
    path('reset_password', ResetPassword.as_view(), name='reset_password'),
    path('reset_password/done', ResetPasswordDone.as_view(), name='reset_password_done'),
    path('reset_password_confirm/<uidb64>/<token>/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),
    path('reset_password/complete', ResetPasswordComplete.as_view(), name='reset_password_complete'),
    # Authentication API
    # path('api/login/', LoginApiView.as_view(), name='login_api'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset_api')),
]