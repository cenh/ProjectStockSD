from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from .models import Supervisor, Project

# This should work but I don't know where to put this class
class AuthorizeUser(ModelBackend):
    def has_perm(self, user_obj, perm, obj):
        if user_obj.is_superuser():
            return True

        if obj is not None:
            if isinstance(obj, User):
                if user_obj == obj:
                    # maybe we should not allow them to delete themselves,
                    # nor add new objects just because obj = user_obj
                    return True
            elif isinstance(obj, Project):
                if user_obj == obj.supervisor.user:
                    return True
            elif isinstance(obj, Supervisor):
                if user_obj == obj.user:
                    return True

        return super(AuthorizeUser, self).has_perm(user_obj, perm, obj)


'''
https://stackoverflow.com/questions/3674463/adding-per-object-permissions-to-django-admin
https://stackoverflow.com/questions/11891606/row-level-permissions-in-django

https://www.ibm.com/developerworks/library/os-django-admin/

DOC
https://docs.djangoproject.com/es/1.9/ref/contrib/auth/
https://docs.djangoproject.com/en/1.9/topics/auth/customizing/#handling-authorization-in-custom-backends
https://github.com/django/django/blob/master/django/contrib/auth/backends.py
'''
