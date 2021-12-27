from django.shortcuts import render
import random
def monday(request):
       #todo_1 = 'Помыть посуду'
      # todo_2 = 'Сделать домашку'
      # todo_3 = 'Погулять'
       todo_list = ['Помыть посуду', 'Сделать домашку', 'Погулять']
       #todo_1 = random.choice(todo_list)
       random.shuffle(todo_list)
       return render(request, 'monday.html', {'todo_list': todo_list})


def tuesday(request):
    # todo_1 = 'Помыть посуду'
    # todo_2 = 'Сделать домашку'
    # todo_3 = 'Погулять'
    todo_list = ['Помыть посуду', 'Сделать домашку', 'Погулять']
    # todo_1 = random.choice(todo_list)
    random.shuffle(todo_list)
    return render(request, 'tuesday.html', {'todo_list': todo_list})

def wednesday(request):
    # todo_1 = 'Помыть посуду'
    # todo_2 = 'Сделать домашку'
    # todo_3 = 'Погулять'
    todo_list = ['Помыть посуду', 'Сделать домашку', 'Погулять']
    # todo_1 = random.choice(todo_list)
    random.shuffle(todo_list)
    return render(request, 'wednesday.html', {'todo_list': todo_list})

def index(request):
    return render(request, 'index.html')


