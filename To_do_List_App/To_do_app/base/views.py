from django.shortcuts import render,redirect
from .models import Task
from .forms import CreateTask
from django.contrib.auth.models import User, auth
from django.contrib import messages
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

def Signup(request):

    if request.method == 'POST':
        first_name = request.POST['First_Name']
        last_name = request.POST['Last_Name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if len(username) == 0 or len(email) ==0 or len(password) ==0 or len(password2)==0 or len(first_name)==0\
            or len(last_name) == 0:
            messages.info(request, 'All fields are mandatory')
            return redirect('signup')
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'UserName Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, 
                                                email=email, 
                                                password=password,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect('login')
        

    return render(request, 'base/signup.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User(email=email, password=password)
        if user.is_authenticated:
            return redirect('/')

    return render(request, 'base/login.html')
    



