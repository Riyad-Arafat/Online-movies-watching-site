from django.db import models
from django import forms
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from slugify import Slugify, UniqueSlugify, slugify, slugify_unicode






class Film(models.Model):
    CATEGORY_OPTIONS = (
        ('افلام', 'افلام'),
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='film_images')
    category = models.CharField(max_length=100,choices=CATEGORY_OPTIONS  ,default='افلام')
    tags = models.ManyToManyField('FilmTags', related_name='films')
    content = models.TextField(max_length=255)
    watch = models.TextField(null=True,default='')
    download_url = models.CharField(max_length=300,null=True,default="#")
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    p = 'افلام'
    def __str__(self):
        return self.title

    readonly_fields = ['category']


    def slug(self):
        return slugify_unicode(self.title,)

    class Meta:
        ordering = ('-created',)



class Series(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='series_images')
    tags = models.ManyToManyField('SeriesTags', related_name='films')
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


    def slug(self):
        return slugify_unicode(self.title,)

    class Meta:
        ordering = ('-created',)

class Episode(models.Model):
    CATEGORY_OPTIONS = (
        ('مسلسلات', 'مسلسلات'),
    )
    title = models.CharField(max_length=255)
    series = models.ForeignKey('Series', on_delete=models.CASCADE,)
    category = models.CharField(max_length=100,choices=CATEGORY_OPTIONS  ,default='مسلسلات')
    image = models.ImageField(default='default.jpg', upload_to='episode_images')
    content = models.TextField()
    watch = models.TextField(null=True,default='')
    download_url = models.CharField(max_length=300,null=True,default="#")
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True)
    views = models.IntegerField(default=0)

    def content(self):
        return self.series.content

    def image(self):
        return self.series.image

    def slug(self):
        return slugify_unicode(self.series.title)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class FilmTags(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def slug(self):
        return slugify_unicode(self.title,)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)




class SeriesTags(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def slug(self):
        return slugify_unicode(self.title,)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def slug(self):
        return slugify_unicode(self.title,)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)
