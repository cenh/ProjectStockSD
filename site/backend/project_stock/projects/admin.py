from django.contrib import admin
from .models import Supervisor, Project, Publication, Group

admin.site.register(Supervisor)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Group)
