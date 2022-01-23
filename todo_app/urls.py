from django.urls import path
from . import views

urlpatterns = [
    path("", views.seeAllTasks, name="seeAll"),
    path("addTask/", views.addTasks, name="addTask"),
    path("updateTask/<int:id>/", views.updateTask, name="update task"),
    path("deleteTask/<int:id>/", views.deleteTask, name="delete task"),
    path("getTask/<int:id>/", views.getSingleTask, name="get task"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]