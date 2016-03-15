# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160314_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subject',
            field=models.CharField(default='No subject', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='description_long',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
