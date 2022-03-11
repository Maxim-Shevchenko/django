"""config URL Configuration

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
from core.views import main
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('moscow', main, name = 'Москва'),
    path('piter', main, name = 'Санкт-Петербург'),
    path('kursk', main, name = 'Курск'),
    path('sevastopol', main, name = 'Севастополь'),
    path('voronezh', main, name = 'Воронеж'),
    path('krasnodar', main, name = 'Краснодар'),
    path('saratov', main, name = 'Саратов')
]
