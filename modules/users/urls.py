""" Urls User """

# Django
from django.urls import path
# Views Users
from .views import UsersListView, UsersAPI, UserUpdateDeleteAPI


urlpatterns = [
    path('', UsersAPI.as_view(), name='user_create_list'),
    path('<int:pk>/', UserUpdateDeleteAPI.as_view(), name='user_udpate_delete'),
    path('list/', UsersListView.as_view(),  name='userList'),
    
]
