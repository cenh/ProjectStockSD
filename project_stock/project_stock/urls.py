from django.conf.urls import include, url, handler404, handler500
from django.contrib import admin
from . import views

handler404 = 'project_stock.views.not_found'
handler500 = 'project_stock.views.bad_request'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^projects/$', views.ProjectView.as_view(), name='project'),
    url(r'^supervisors/$', views.SupervisorView.as_view(), name='supervisor'),
    url(r'^groups/$', views.GroupView.as_view(), name='group'),

    url(r'^supervisors/(?P<pk>[0-9]+)', views.SupervisorDetailView.as_view(), name='supervisor'),
    url(r'^projects/(?P<pk>[0-9]+)', views.ProjectDetailView.as_view(), name='project'),
    url(r'^groups/(?P<pk>[0-9]+)', views.GroupDetailView.as_view(), name='group'),

    url(r'^admin/', admin.site.urls),
]
