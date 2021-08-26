"""PersonalSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import PersonalSite.views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('resume/', TemplateView.as_view(template_name='resume.html'), name='resume'),
    path('achievements/', TemplateView.as_view(template_name='achievements.html'),
         name='achievements'),
    path('about/', TemplateView.as_view(template_name='about.html'),
         name='about'),
    path('projects/', TemplateView.as_view(template_name='projects.html'), name='projects'),
    path('work/', TemplateView.as_view(template_name='work.html'),
         name='work'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('blog/', include('blog.urls'), name='blog'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
