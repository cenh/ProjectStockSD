from django.conf.urls import url
from . import views

urlpatterns = [
    # projects
    url(r'^projects/$', views.ProjectView.as_view(), name='project'),
    
    # supervisors
    url(r'^supervisors/$', views.SupervisorView.as_view(), name='supervisor'),

    # /supervisors/ID
    url(r'^supervisors/(?P<pk>[0-9]+)', views.SupervisorDetailView.as_view() , name='supervisor'),

    # /projects/ID
    url(r'^projects/(?P<pk>[0-9]+)', views.ProjectDetailView.as_view() , name='project'),

    # /projects/ or /supervisors/
    url(r'^$', views.ProjectView.as_view(), name='project'),
]
