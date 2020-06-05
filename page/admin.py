from django.contrib import admin
from .models import Film, Series, Episode,FilmTags,SeriesTags,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ['created','publish']
    list_display =['title','created','publish']


class EpisodeAdmin(admin.ModelAdmin):
    list_filter = ['created','publish']
    list_display =['title','publish','created']

admin.site.register(FilmTags)
admin.site.register(SeriesTags)
admin.site.register(Film, PostAdmin)
admin.site.register(Series, PostAdmin)
admin.site.register(Episode, EpisodeAdmin)
admin.site.register(Category)

