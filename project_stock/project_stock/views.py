from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Project, Supervisor, Group, Publication
from django.views import generic
from django.db.models import Count
from django.utils import timezone
from django.template import RequestContext

def not_found(request):
    response = render_to_response('status/404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response

def bad_request(request):
    response = render_to_response('status/500.html', context_instance=RequestContext(request))
    response.status_code = 500
    return response

class IndexView(generic.ListView):
    model = Project
    template_name = 'index.html'

    def get_queryset(self):
        return Project.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        context['supervisor_list'] = Supervisor.objects.filter(project__deadline__gte=timezone.now()) \
                                                       .annotate(num_projects=Count('project')) \
                                                       .order_by('-num_projects')[0:5]
        context['random_project_list'] = Project.objects.filter(deadline__gte=timezone.now()).order_by('?')[:1]
        context['project_bachelor'] = Project.objects.filter(deadline__gte=timezone.now()).filter(type='B').order_by('-pub_date')[:5]
        context['project_master'] = Project.objects.filter(deadline__gte=timezone.now()).filter(type='M').order_by('-pub_date')[:5]
        context['project_thesis'] = Project.objects.filter(deadline__gte=timezone.now()).filter(type='T').order_by('-pub_date')[:5]
        return context

class ProjectView(generic.ListView):
    model = Project
    template_name = 'projects/index.html'

    def get_queryset(self):
        return Project.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['active_projects'] = Project.objects.filter(deadline__gte=timezone.now()).order_by('name')
        context['inactive_projects'] = Project.objects.filter(deadline__lte=timezone.now()).exclude(deadline=timezone.now()).order_by('name')
        return context

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
        context['active_projects'] = Project.objects.filter(deadline__gte=timezone.now()).order_by('name')
        context['inactive_projects'] = Project.objects.filter(deadline__lte=timezone.now()).exclude(deadline=timezone.now()).order_by('name')
        context['group_list'] = Group.objects.order_by('id')
        return context

class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'groups/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        context['supervisor_list'] = Supervisor.objects.order_by('last_name')
        return context

class RegistrationView(generic.ListView):
    model = Supervisor
    template_name = 'registration/index.html'

    def get_queryset(self):
        return Supervisor.objects.order_by('email')
