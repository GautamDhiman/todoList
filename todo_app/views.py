from ast import Try
from django.shortcuts import render, HttpResponse
from .models import Task
from .forms import taskForm
from django.http import JsonResponse
from sentry_sdk import capture_exception, capture_message

# Create your views here.

def seeAllTasks(request):

    try:
        allTasks = Task.objects.all().values()
    except Exception as e:
        # Alternatively the argument can be omitted
        capture_message('Something went wrong')
        capture_exception(e)
     
    allTasks_list = list(allTasks)  # important: convert the QuerySet to a list object
    print(allTasks_list)
    
    return JsonResponse(allTasks_list, safe=False)

    # GET
    # return HttpResponse('All tasks')

def addTasks(request):
    
    #Post
    return HttpResponse("add tasks")

def getSingleTask(request, id):

    try:
        getTasks = Task.objects.all().values()
    except Exception as e:
        # Alternatively the argument can be omitted
        capture_message('Something went wrong')
        capture_exception(e)
    
    getTasks_list = list(getTasks)  # important: convert the QuerySet to a list object
    print(getTasks_list)
    
    return JsonResponse(getTasks_list[id-1], safe=False)
    #Get
    # return HttpResponse("get single task")

def updateTask(request, id):

    
    #POST
    return HttpResponse("Update task")

def deleteTask(request, id):

    #Get
    return HttpResponse("Delete task {0}".format(id))