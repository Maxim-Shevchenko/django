from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def main(request):
    path = request.path
    path = path.replace('/', '')
    if path == "":
        path = 'main'
    cities = ['Москва', 'Санкт-Петербург', 'Курск', 'Севастополь', 'Воронеж', 'Краснодар', 'Саратов']
    return render(request, f'{path}.html', {'cities':cities})