from django.shortcuts import render, HttpResponse, redirect
from .models import Task
from .forms import taskForm
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def seeAllTasks(request):
    
    allTasks = Task.objects.all().values() 
    allTasks_list = list(allTasks)  # important: convert the QuerySet to a list object
    print(allTasks_list)
    
    return JsonResponse(allTasks_list, safe=False)

    # GET
    # return HttpResponse('All tasks')

@login_required(login_url='login')
def addTasks(request):
    
    #Post
    return HttpResponse("add tasks")

@login_required(login_url='login')
def getSingleTask(request, id):

    getTasks = Task.objects.all().values()
    getTasks_list = list(getTasks)  # important: convert the QuerySet to a list object
    print(getTasks_list)
    
    return JsonResponse(getTasks_list[id-1], safe=False)
    #Get
    # return HttpResponse("get single task")

@login_required(login_url='login')
def updateTask(request, id):

    
    #POST
    return HttpResponse("Update task")

@login_required(login_url='login')
def deleteTask(request, id):

    #Get
    return HttpResponse("Delete task {0}".format(id))