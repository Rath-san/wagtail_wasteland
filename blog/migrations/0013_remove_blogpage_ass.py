# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-01 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_blogpage_ass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='ass',
        ),
    ]
