from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
# Create your views here.
x=ListView

class TaskList(ListView):
    model = Task
