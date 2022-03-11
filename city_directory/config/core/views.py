from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def main(request):
    cities = ['Москва', 'Санкт-Петербург', 'Курск', 'Севастополь', 'Воронеж', 'Краснодар', 'Саратов']
    return render(request, 'main.html', {'cities':cities})