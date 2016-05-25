from django.contrib import admin
from .models import Supervisor, Project, Publication, Group
from django.contrib.admin import ModelAdmin
from .forms import PhotoModelForm
from base64 import b64encode

class PhotoModelAdmin(ModelAdmin):
    """ModelAdmin that overrides the default ModelForm in the admin site"""
    form = PhotoModelForm

    def save_model(self, request, obj, form, change):
        if request.method == 'POST':
            obj.photo = b64encode(request.FILES['photo_file'].read())
            obj.save()

# PhotoModelAdmin handles photo upload and conversion to base64
admin.site.register(Supervisor, PhotoModelAdmin)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Group)
