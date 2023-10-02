from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def lists(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "todolist/index.html", {
        "tasks": request.session["tasks"],
    })


def add(request):
    if request.method == "POST":
        task = request.POST["task"].strip()
        if task:
            todo = task
            request.session["tasks"] += [todo]
            return HttpResponseRedirect(reverse('todoList:todos'))
        else:
            return render(request, "todolist/add.html")
    return render(request, "todolist/add.html")
