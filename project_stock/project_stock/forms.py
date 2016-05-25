from django.forms import ModelForm, FileField
from .models import Supervisor

class PhotoModelForm(ModelForm):
    """A Supervisor Modelform that handles a file upload into memory, converts
       it to base64, and finally saves it into the database as a string
    """
    photo_file = FileField(required=False)

    class Meta:
        model = Supervisor
        exclude = ['photo']
