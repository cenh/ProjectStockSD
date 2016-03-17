from django.db import models
from django.core.validators import RegexValidator

class Supervisor(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    website = models.CharField(max_length=128, blank=True)
    location = models.CharField(max_length=128, blank=True) # office
    workplace = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=128, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=15) # validators should be a list

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Project(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=64)
    description_short = models.CharField(max_length=256)
    description_long = models.TextField()
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.name
