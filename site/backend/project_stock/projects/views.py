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


class SupervisorDetailView(generic.DetailView):
    model = Supervisor
    template_name = 'supervisors/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SupervisorDetailView, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.all()

        return context

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/profile.html'
