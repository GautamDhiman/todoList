from django.shortcuts import render, HttpResponse
from .models import Task
from django.http import JsonResponse

# Create your views here.

def seeAllTasks(request):
    
    allTasks = Task.objects.all().values() 
    allTasks_list = list(allTasks)  # important: convert the QuerySet to a list object
    print(allTasks_list)
    
    return JsonResponse(allTasks_list, safe=False)

    # GET
    # return HttpResponse('All tasks')

def addTasks(request):
    
    #Post
    return HttpResponse("add tasks")

def getSingleTask(request, id):

    getTasks = Task.objects.all().values()
    getTasks_list = list(getTasks)  # important: convert the QuerySet to a list object
    print(getTasks_list)
    
    return JsonResponse(getTasks_list[id-1], safe=False)
    #Get
    # return HttpResponse("get single task")

def updateTask(request, id):


    #Get
    return HttpResponse("Update task")

def deleteTask(request, id):

    #Get
    return HttpResponse("Delete task {0}".format(id))