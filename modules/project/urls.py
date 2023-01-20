""" Urls core """

# Django
from django.urls import path
# Views Users
from  .views import ProjectsListView , ProjectAPI, ProjectUpdateDeleteAPI


urlpatterns = [
    # user CRUD
    path('', ProjectAPI.as_view(), name='projects_api'),
    path('list/', ProjectsListView.as_view(), name='projectList'),
    path('<int:pk>/', ProjectUpdateDeleteAPI.as_view(), name='project_udpate_delete'),
]
