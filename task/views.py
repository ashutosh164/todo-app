from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from  django.contrib import messages
# Create your views here.


def index(request):
    task = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Update success')

            return redirect("/")

    return render(request, 'index.html',{'task':task,'form':form})


def update(request,pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update success')
        return redirect('/')

    return render(request,'update.html',{'form':form})


def delete(request,pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.info(request,'Are you sure to delete')
        return redirect("/")

    return render(request,'delete.html',{'item':item})


def register(request):

    form = CustomerForm()
    return render(request,'register.html',{'form':form})


def login(request):
    return render(request,'login.html')