from django.db import models
from django.core.validators import RegexValidator

class Supervisor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    website = models.URLField(max_length=128, blank=True, null=True)
    location = models.CharField(max_length=128, blank=True, null=True) # office
    workplace = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=128, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True) # validators should be a list
    mobile = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    fax = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)

    # this is a base64 field. Easy to scrape and link but how to manage from admin page?
    # 2^25 should be about 32MB in characters
    photo = models.TextField(max_length=2**25, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Project(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=64)
    type_choices = (('B', 'Bachelor project'),
                    ('M', 'Master\'s project'),
                    ('T', 'Master\'s thesis'),
                    ('C', 'Project with compay'),
                    ('O', 'Other'))
    type = models.CharField(max_length=1, choices=type_choices)
    subject = models.CharField(max_length=128)
    description_short = models.TextField(max_length=256, blank=True, null=True, verbose_name='Short description')
    description_long = models.TextField(blank=True, null=True, verbose_name='Long description')
    website = models.URLField(max_length=128, blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
'''
class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Presentations(models.Model):
    person = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField()
    website = models.URLField(max_length=128)

    def __str__(self):
        return self.name
'''
