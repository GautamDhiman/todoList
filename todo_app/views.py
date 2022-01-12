from django.shortcuts import render

# Create your views here.

def seeAllTasks(request):
    
    # GET
    return HttpResponse('All tasks')

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