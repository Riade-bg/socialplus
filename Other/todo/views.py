from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all().order_by("-id")
    contex = {
        'obj': todos
    }
    return render(request, "index.html", contex)

def add_todo(request):
    content = request.POST.get('Search')
    time = timezone.now()
    todo = Todo.objects.create(text = content, date_field = time)
    return HttpResponseRedirect("/")

def delete(request, id):
    Todo.objects.get(id=id).delete()
    return HttpResponseRedirect("/")

