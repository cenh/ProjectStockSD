from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.views import generic

class IndexView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Project.objects.order_by('id')
