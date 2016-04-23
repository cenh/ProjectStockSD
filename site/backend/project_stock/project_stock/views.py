from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Supervisor, Group, Publication
from django.views import generic

class IndexView(generic.ListView):
    model = Project
    template_name = 'index.html'

    def get_queryset(self):
        return Project.objects.order_by('pub_date')

class ProjectView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

    def get_queryset(self):
        return Project.objects.order_by('name') #Descending

class SupervisorView(generic.ListView):
    model = Supervisor
    template_name = 'supervisors/index.html'

    def get_queryset(self):
        return Supervisor.objects.order_by('last_name')

class GroupView(generic.ListView):
    model = Group
    template_name = 'groups/index.html'

    def get_queryset(self):
        return Group.objects.order_by('name')

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'projects/profile.html'

class SupervisorDetailView(generic.DetailView):
    model = Supervisor
    template_name = 'supervisors/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SupervisorDetailView, self).get_context_data(**kwargs)
        context['project_list'] = Project.objects.order_by('name')

        return context

class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'groups/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['supervisor_list'] = Supervisor.objects.order_by('last_name')

        return context

