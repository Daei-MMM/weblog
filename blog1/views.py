from django.shortcuts import render , get_object_or_404
from .models import post , todo
from django.http import HttpRequest,HttpResponse , HttpResponseRedirect
from django import forms
from .forms import CreateForms , TodoForm
from datetime import datetime
# Create your views here.

def index(requset: HttpRequest):
    return HttpResponse('<p style="color:#FF0000";>Red paragraph text</p>')



def index2(requset:HttpRequest):
    all=post.objects.all()
    return render(requset, 'blog1/index2.html',{'all':all})

def create(request):

    if request.method == "POST":
        cfrm = CreateForms(request.POST)
        if cfrm.is_valid():
            frm1=cfrm.cleaned_data
            post.objects.create(title=frm1['title'],text=frm1['text'],date=datetime.now()) 
            return HttpResponseRedirect('/create/')
    else:  
        frm=CreateForms()
        return render(request ,'blog1/create.html',{'frm':frm})


def todos(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            todo.objects.create(title=cd['title'],text= cd['text'])
            return HttpResponseRedirect('/admin/')
    else:
        todos = TodoForm()
    
    return render(request,'blog1/todo.html',{'todo':todos})


def main1(request:HttpRequest):
    return render(request,'blog1/main.html')


    