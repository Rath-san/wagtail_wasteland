# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
# from wagtailclearstream.stream import ClearBlock #heh
# from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index

from wagtail.contrib.table_block.blocks import TableBlock

from wagtail.wagtailsnippets.models import register_snippet

# Create your models here.

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super(BlogIndexPage, self).get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')

class BlogTagIndexPage(Page):

    def get_context(self, request):
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        context = super(BlogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context

class BlogPage(Page):

    new_table_options = {
        'minSpareRows': 0,
        'startRows': 6,
        'startCols': 4,
        'colHeaders': False,
        'rowHeaders': False,
        'contextMenu': True,
        'editor': 'text',
        'stretchH': 'all',
        'height': 216,
        'language': 'en',
        'renderer': 'text',
        'autoColumnSize': False,
    }

    BLOCK_CHOICES = [
        ('choices1','choices1'),
        ('choices1','choices1'),
        ('choices1','choices1'),
        ('choices1','choices1')
    ]

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('CharBlock', blocks.CharBlock(classname="full title")),
        ('TextBlock', blocks.TextBlock()),
        ('EmailBlock', blocks.EmailBlock()),
        ('IntegerBlock', blocks.IntegerBlock()),
        ('FloatBlock', blocks.FloatBlock()),
        ('DecimalBlock', blocks.DecimalBlock()),
        ('URLBlock', blocks.URLBlock()),
        ('BooleanBlock', blocks.BooleanBlock()),
        ('DateBlock', blocks.DateBlock()),
        ('TimeBlock', blocks.TimeBlock()),
        ('DateTimeBlock', blocks.DateTimeBlock()),
        ('RawHTMLBlock', blocks.RawHTMLBlock()),
        ('BlockQuoteBlock', blocks.BlockQuoteBlock()),
        ('ChoiceBlock', blocks.ChoiceBlock(required=False, choices=BLOCK_CHOICES)),
        ('PageChooserBlock', blocks.PageChooserBlock(required=False)),
        # ('DocumentChooserBlock', blocks.DocumentChooserBlock()),
        ('RichtextBlock', blocks.RichTextBlock()),
        ('ImageChooserBlock', ImageChooserBlock(required=False)),
        # ('EmbedBlock', blocks.EmbedBlock()),
        ('StaticBlock', blocks.StaticBlock()),
        ('Table', TableBlock()),
    ])

    RichTextField(blank=True)

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel (
            [
                FieldPanel('date'),
                FieldPanel('tags'),
                FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            ], heading='Blog page tags'
        ),
        MultiFieldPanel (
            [
                FieldPanel('intro'),
                InlinePanel('gallery_images', label='Gallery images')
            ],heading="Blog page content", classname="collapsible"
        ),
        StreamFieldPanel('body')
    ]

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+"
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "blog categories"
