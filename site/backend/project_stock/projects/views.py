from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Supervisor
from django.views import generic

class ProjectView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

    def get_queryset(self):
        return Project.objects.order_by('id')

    class SupervisorView(generic.ListView):
    model = Supervisor
    template_name = 'supervisors/index.html'

    def get_queryset(self):
        return Supervisor.objects.order_by('id')
'''
class SupervisorDetailView(generic.DetailView, supervisor_id):
    model = Supervisor
    template_name = 'supervisors/profile.html'

    def get_queryset(self):
        return Supervisor.objects.get(pk=supervisor_id)

class ProjectDetailView(generic.DetailView, project_id):
    model = Project
    template_name = 'projects/profile.html'

    def get_queryset(self):
        return Project.objects.get(pk=project_id)
'''
