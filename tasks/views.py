from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    mods = Task.objects.all()

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'mods': mods, 'form': form}
    return render(request, "tasks/index.html", context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/updatetodo.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':
        print('imhere')
        form = TaskForm(request.POST, instance=task)
        task.delete()
        return redirect('/')
    context = {'task': task}
    return render(request, 'tasks/delete.html', context)
