from django.conf.urls import url
from . import views

urlpatterns = [
    # /projects/projects
    url(r'^projects/', views.ProjectView.as_view(), name='project'),

    # /projects/supervisors
    url(r'^supervisors/', views.SupervisorView.as_view(), name='supervisor'),

    # /projects/ or /supervisors/
    url(r'^$', views.ProjectView.as_view(), name='project'),
]
