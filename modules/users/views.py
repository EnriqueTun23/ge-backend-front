""" Views administrative user panel """

# Django 
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import redirect
# Django REST Framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework import status
# EMail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes
from django.http import HttpResponse
# Token generator 
from .token import account_activation_token

# models
from .models import User
# serializer
from .serializer import UserSerializer

""" ----- CRUD USER ----- """

class UsersListView(ListView):
    """ List Users """
    template_name = 'users/administrador/users.html'
    context_object_name = 'users'
    model = User

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            users = self.model.objects.filter(Q(last_name__icontains=query) | Q(first_name__icontains=query ))
            #users = self.model.objects.filter(login__last_name__icontains=query)
        else:
            users = self.model.objects.all()
        
        return users


class UsersAPI(ListCreateAPIView):
    model = User
    queryset = User
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        data =  self.queryset.objects.all()
        employee = self.request.query_params.get('employee', None)
        client = self.request.query_params.get('client', None)
        if employee is not None:
            data = data.filter(userPerson__employee=employee)
        
        if client is not None:
            data = data.filter(userPerson__client=client)

        return data

    def post(self, request, *args, **kwargs):
        serializerUser = UserSerializer(data=request.data)
        if serializerUser.is_valid(raise_exception=True):
            user = serializerUser.save()
            user.is_verified = False
            user.save()
            subject = 'Activar cuenta.'
            from_email = 'projects.midsoftware@gmail.com'
            current_site =  get_current_site(request)
            body = render_to_string('users/email/acc_active_email.html', {
                'user':  user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
                'protocol': request.is_secure()
            })
            to_email = serializerUser.validated_data.get('email')
            email = EmailMultiAlternatives(subject, body, from_email, [to_email])
            if 'users/email/acc_active_email.html' is not None:
                html_email = render_to_string('users/email/acc_active_email.txt', {
                'user':  user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
                'protocol': request.is_secure()
            })
                email.attach_alternative(html_email, 'text/html')
            # import pdb; pdb.set_trace()
            email.send()
            return Response(serializerUser.data, status=status.HTTP_201_CREATED)
        else:
            return HttpResponse('nose pudo guardar')


class UserUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = User.objects.get(pk=pk)
        obj.userRol.delete()
        obj.userPerson.delete()
        obj.delete()
        
        return self.destroy(request, *args, **kwargs)