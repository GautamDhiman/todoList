from django.shortcuts import render, HttpResponse
from .models import Task
from django.http import JsonResponse


# Create your views here.

def seeAllTasks(request):
    
    allTasks = Task.objects.all().values()

    allTasks_list = list(allTasks)  # important: convert the QuerySet to a list object
    return JsonResponse(allTasks_list, safe=False)

def addTasks(request):
    
    #Post
    return HttpResponse("add tasks")

def getSingleTask(request, id):


    #Get
    return HttpResponse("get single task")

def updateTask(request, id):


    #Get
    return HttpResponse("Update task")

def deleteTask(request, id):

    #Get
    return HttpResponse("Delete task {0}".format(id))