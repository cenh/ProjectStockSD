"""project_stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', p_views.ProjectView.as_view(), name='project'),

    url(r'^projects/$', p_views.ProjectView.as_view(), name='project'),
    url(r'^supervisors/$', p_views.SupervisorView.as_view(), name='supervisor'),
    url(r'^groups/$', p_views.GroupView.as_view(), name='group'),

    url(r'^supervisors/(?P<pk>[0-9]+)', p_views.SupervisorDetailView.as_view(), name='supervisor'),
    url(r'^projects/(?P<pk>[0-9]+)', p_views.ProjectDetailView.as_view(), name='project'),
    url(r'^groups/(?P<pk>[0-9]+)', p_views.GroupDetailView.as_view(), name='group'),

    url(r'^admin/', admin.site.urls),
    url(r'^example/$', views.example, name='example'),
]
