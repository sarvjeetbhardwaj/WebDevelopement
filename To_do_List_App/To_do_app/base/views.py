from django.shortcuts import render,redirect
from .models import Task
from .forms import CreateTask
from django.contrib.auth.models import User, auth

from django.contrib.auth.views import LoginView


def TaskList(request):
    task_list = Task.objects.all()
    return render(request,'base/task_list.html',{'task_list':task_list})

def TaskDetail(request, pk):
    task_detail = Task.objects.get(id = pk)
    return render(request,'base/task_details.html',{"task_detail":task_detail})

def TaskCreate(request):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'base/task_create.html', {'createtask':form})

def TaskUpdate(request,pk):

    task = Task.objects.get(id=pk)
    form = CreateTask(instance=task)

    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task, files=request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('/')

    return render(request, 'base/task_update.html', {'updateform':form, 'task':task})

def DeleteConfirmation(request,pk):

    task = Task.objects.get(id=pk)
    return render(request, 'base/delete_confirmation.html',{'task':task})
    
def TaskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('/')
    



