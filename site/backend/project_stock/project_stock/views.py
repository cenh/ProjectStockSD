from django.shortcuts import render
from django.http import HttpResponse

def example(request):
    return render(request, 'templates/project_stock/example.html')
