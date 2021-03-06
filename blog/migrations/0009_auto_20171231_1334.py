# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-31 12:34
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.blocks.static_block
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171231_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('CharBlock', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('TextBlock', wagtail.wagtailcore.blocks.TextBlock()), ('EmailBlock', wagtail.wagtailcore.blocks.EmailBlock()), ('IntegerBlock', wagtail.wagtailcore.blocks.IntegerBlock()), ('FloatBlock', wagtail.wagtailcore.blocks.FloatBlock()), ('DecimalBlock', wagtail.wagtailcore.blocks.DecimalBlock()), ('URLBlock', wagtail.wagtailcore.blocks.URLBlock()), ('BooleanBlock', wagtail.wagtailcore.blocks.BooleanBlock()), ('DateBlock', wagtail.wagtailcore.blocks.DateBlock()), ('TimeBlock', wagtail.wagtailcore.blocks.TimeBlock()), ('DateTimeBlock', wagtail.wagtailcore.blocks.DateTimeBlock()), ('RawHTMLBlock', wagtail.wagtailcore.blocks.RawHTMLBlock()), ('BlockQuoteBlock', wagtail.wagtailcore.blocks.BlockQuoteBlock()), ('ChoiceBlock', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('choices1', 'choices1'), ('choices1', 'choices1'), ('choices1', 'choices1'), ('choices1', 'choices1')], required=False)), ('PageChooserBlock', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('RichtextBlock', wagtail.wagtailcore.blocks.RichTextBlock()), ('ImageChooserBlock', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), ('StaticBlock', wagtail.wagtailcore.blocks.static_block.StaticBlock())]),
        ),
    ]
