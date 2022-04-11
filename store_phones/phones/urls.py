from django.contrib import admin
from django.urls import path, include
from phones.views import home
from django.views.generic import TemplateView
from phones.views import PhoneListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PhoneListView.as_view(), name='home')
]