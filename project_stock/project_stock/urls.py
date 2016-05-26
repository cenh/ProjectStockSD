from django.conf.urls import include, url, handler404, handler500
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from . import views

handler404 = 'project_stock.views.not_found'
handler500 = 'project_stock.views.bad_request'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^projects/$', views.ProjectListView.as_view(), name='project'),
    url(r'^projects/inactive$', views.InactiveProjectListView.as_view(), name='inactive_project'),
    url(r'^supervisors/$', views.SupervisorListView.as_view(), name='supervisor'),
    url(r'^groups/$', views.GroupListView.as_view(), name='group'),

    url(r'^supervisors/(?P<pk>[0-9]+)', views.SupervisorDetailView.as_view(), name='supervisor'),
    url(r'^projects/(?P<pk>[0-9]+)', views.ProjectDetailView.as_view(), name='project'),
    url(r'^groups/(?P<pk>[0-9]+)', views.GroupDetailView.as_view(), name='group'),

    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),

    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
