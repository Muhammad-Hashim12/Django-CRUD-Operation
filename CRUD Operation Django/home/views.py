from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    if request.method=='POST':
        id=request.POST['id']
        data1=request.POST['data1']
        data2=request.POST['data2']
        Entry(id=id,data1=data1,data2=data2).save()
        msg='data is been saved'
        
        return render(request,'home.html',{'msg':msg})
    else:
        return render(request,'home.html')

def show(request):
    data= Entry.objects.all()
    return render(request,'show.html',{'data':data})

def delete(request):
    id=request.GET['id']
    Entry.objects.filter(id=id).delete()
    return redirect('show')

def edit(request):
    id=request.GET['id']
    data1 = data2 = "Not_availbale"
    for data in Entry.objects.filter(id=id):
        data1=data.data1
        data2=data.data2
    return render(request,'edit.html',{'id':id,'data1':data1,'data2':data2})

def recordedited(request):
    id=request.POST['id']
    data1=request.POST['data1']
    data2=request.POST['data2']
    Entry.objects.filter(id=id).update(id=id,data1=data1,data2=data2)
    return redirect('show')