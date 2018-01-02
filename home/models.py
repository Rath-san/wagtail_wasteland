from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


class HomePage(Page):

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'

    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )

    body = RichTextField(blank=True)
    select = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)

    content_panels = Page.content_panels + [
        MultiFieldPanel (
            [
                FieldPanel('select', classname="full"),
                FieldPanel('body', classname="full")
            ], heading="Some heading", classname="collapsible collapsed"
        )
    ]

    def is_upperclass(self):
        return self.select in (self.JUNIOR, self.SENIOR)
