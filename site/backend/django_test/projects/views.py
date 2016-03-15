from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def index(request):
    context = {'project_list': Project.objects.order_by('id')}
    return render(request, 'projects/index.html', context)
