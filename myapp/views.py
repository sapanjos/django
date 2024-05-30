from django.shortcuts import render
from .models import TodoItem
def home(request):
    return render(request, 'home.html')

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {'todos': items})