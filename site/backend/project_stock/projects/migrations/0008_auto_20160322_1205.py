# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 11:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20160322_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('B', 'Bachelor project'), ('M', "Master's project"), ('T', "Master's thesis"), ('C', 'Project with compay'), ('O', 'Other')], default='O', max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='location',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='status',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='website',
            field=models.URLField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='supervisor',
            name='workplace',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
