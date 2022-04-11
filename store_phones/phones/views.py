from django.shortcuts import render
from django.views.generic import ListView
from phones.models import Phone


class PhoneListView(ListView):
    model = Phone
    template_name = 'phones/home.html'
    context_object_name = 'phone_list'


def home(request):
    return render(request, 'home.html')

# Create your views here.
