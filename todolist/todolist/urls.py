"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from core.views import index
from core.views import monday
from core.views import tuesday
from core.views import wednesday
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('monday', monday),
    path('tuesday', tuesday),
    path('wednesday', wednesday),
    path('', TemplateView.as_view(template_name='index.html')),
    path('monday', TemplateView.as_view(template_name='monday.html')),
    path('tuesday', TemplateView.as_view(template_name='tuesday.html')),
    path('wednesday', TemplateView.as_view(template_name='wednesday.html')),
    path('thursday', TemplateView.as_view(template_name='thursday.html')),
    path('friday', TemplateView.as_view(template_name='friday.html')),
    path('saturday', TemplateView.as_view(template_name='saturday.html')),
    path('sunday', TemplateView.as_view(template_name='sunday.html')),

]
