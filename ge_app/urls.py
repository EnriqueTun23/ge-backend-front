"""ge_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Django
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

#ejemplo
from django.views.generic import TemplateView


urlpatterns = [
    path('ge/', include('modules.core.urls')),
    path('ge/users/', include('modules.users.urls')),
    path('ge/clients/', include('modules.clients.urls')),
    path('ge/projects/', include('modules.project.urls')),
    path('ge/files/', include('modules.files.urls')),
    path('ge/postales/', include('modules.cp.urls')),
    path('ge/roles/', include('modules.roles.urls')),
    path('ge/admin/', admin.site.urls),
    # ----------- Prueba de login and reset --------
    #path('ge/accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)