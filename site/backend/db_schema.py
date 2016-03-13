from django.db import models

class Member(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    website = models.URLField(max_length=128)
    location = models.CharField(max_length=128) # office
    workplace = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    tel = models.IntegerField() # 004512345678
    biography = models.TextField()

    def __str__(self):
        return self.name

class Articles(models.Model):
    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    description = models.TextField()
    website = models.URLField(max_length=128)

    def __str__(self):
        return self.name

class Presentations(models.Model):
    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.TextField(max_length=128)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    website = models.URLField(max_length=128)

    def __str__(self):
        return self.name

class Activities(models.Model):
    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    category = models.CharField(max_length=128)
    organisation = models.CharField(max_length=128)
    title = models.TextField(max_length=128)
    website = models.URLField(max_length=128)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Member, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Project(models.Model):
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    deadline = models.DateField(auto_now=False, auto_now_add=False)
    subject = models.CharField(max_length=128)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
