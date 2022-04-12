from django.contrib import admin
from django.urls import path, include
from phones.views import home
from django.views.generic import TemplateView
from phones.views import PhoneListView, PhoneDetailView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PhoneListView.as_view(), name='home'),
    path('<slug:slug>/', PhoneDetailView.as_view(), name='phone_detail'),
]