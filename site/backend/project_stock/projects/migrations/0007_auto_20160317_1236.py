# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160315_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='email',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='first_name',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='last_name',
            field=models.CharField(max_length=32),
        ),
    ]
