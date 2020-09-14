from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from .forms import *

# Create your views here.
def index(request):
    '''The home page for our ToDo app'''
    lists=List.objects.all()

    form=ListForm()

    if request.method=='POST':
        form=ListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={'lists':lists, 'form':form}
    return render(request, 'ToDo_App/index.html', context)

def new_list(request):
    """Adding an new list of items"""
    if request.method!='POST':
        form=ListForm()
    else:
        form=ListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('ToDo_App:index')
    context={'form': form}
    return render(request, 'ToDo_App/new_list.html', context)
