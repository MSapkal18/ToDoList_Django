from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def home(req):
    tasks=Task.objects.all().order_by('created')
    totalTask = Task.objects.filter(completed=False).count()
    return render(req,'home.html',{"tasks": tasks,"totalTask":totalTask})

def addTask(req):
    obj=Task()
    obj.title=req.POST.get('title')
    obj.save()
    return redirect("home")
def deleteTask(req,task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect("home")
def completeTask(req,task_id):
    task=Task.objects.get(id=task_id)
    task.completed=not task.completed
    task.save()
    return redirect("home")
def newOne(req):
    return HttpResponse("Hello")

