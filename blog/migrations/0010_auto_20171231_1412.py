# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 13:12
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171231_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('CharBlock', wagtail.wagtailcore.blocks.CharBlock(classname='full title'))]),
        ),
    ]