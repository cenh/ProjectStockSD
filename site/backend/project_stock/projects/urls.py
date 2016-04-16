from django.conf.urls import url
from . import views

urlpatterns = [
    # /projects/ or /supervisors/
    url(r'^$', views.ProjectView.as_view(), name='project'),

    # /projects/
    url(r'^projects/$', views.ProjectView.as_view(), name='project'),

    # /supervisors/
    url(r'^supervisors/$', views.SupervisorView.as_view(), name='supervisor'),

    # /groups/
    url(r'^groups/$', views.GroupView.as_view(), name='group'),

    # /projects/ID
    url(r'^projects/(?P<pk>[0-9]+)', views.ProjectDetailView.as_view(), name='project'),

    # /supervisors/ID
    url(r'^supervisors/(?P<pk>[0-9]+)', views.SupervisorDetailView.as_view(), name='supervisor'),

    # /groups/ID
    url(r'^groups/(?P<pk>[0-9]+)'. views.GroupDetailView.as_view(), name='group'),

]
