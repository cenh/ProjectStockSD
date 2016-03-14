from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Django er skide fedt man!")
