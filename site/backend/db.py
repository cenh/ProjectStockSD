from django.db import models

class Member(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    website = models.CharField(max_length=128)
    location = models.CharField(max_length=128) # office
    workplace = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    tel = models.IntegerField() # 004512345678

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
