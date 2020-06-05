from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Film,Series,Episode,FilmTags,SeriesTags,Category
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User
from itertools import chain



def search(request):
    try:
        search = request.GET.get("search")

    except:
        search = None
    if search:
        context = {
            'query': search,
            'films' : Film.objects.filter(publish=True,title__contains=search),
            'series1': Series.objects.filter(publish=True,title__contains=search)
        }
        template = 'search.html'
    else:
        template = 'index.html'
        context = {
            "title": 'Electredo',
            'film_tags': FilmTags.objects.all(),
            'series_tags': SeriesTags.objects.all(),
            "films": Film.objects.filter(publish=True),
            'episodes': Episode.objects.filter(publish=True),
            'series1': Series.objects.filter(publish=True),

        }

    return render(request , template, context)


def home(request):
    films = Film.objects.filter(publish=True)
    episodes = Episode.objects.filter(publish=True)
    paginator_films = Paginator(films, 15)
    paginator_episodes = Paginator(episodes, 15)
    page = request.GET.get('page')
    try:
        films = paginator_films.page(page)
        episodes = paginator_episodes.page(page)
    except PageNotAnInteger:
        films = paginator_films.page(1)
        episodes = paginator_episodes.page(1)
    except EmptyPage:
        films = paginator_films.page(paginator.num_page)
        episodes = paginator_episodes.page(paginator.num_page)



    template = 'index.html'
    context = {
        "title" : 'Electredo',
        'categories': Category.objects.all(),
        'film_tags': FilmTags.objects.all(),
        'series_tags':SeriesTags.objects.all(),
        "films" : films,
        'episodes' : episodes,
        'series1' : Series.objects.filter(publish=True),

    }
    return render(request, template, context)

def film_page(request, film_id, film_slug):
    film = get_object_or_404(Film, pk=film_id)
    film.views = film.views + 1
    film.save()
    template = 'film.html'
    context = {
        'title' : film.title,
        'film' : film,
    }
    return  render(request, template, context)


def series_page(request, series_id, series_slug ):
    series = get_object_or_404(Series, pk=series_id)
    series.views = series.views + 1
    series.save()
    template = 'series.html'
    context = {
        'title' : series.title,
        'series' : series,
        'episodes' : Episode.objects.filter(publish=True,series=series.id)
    }
    return  render(request, template, context)

def episode_page(request, episode_slug, episode_id):
    episode = get_object_or_404(Episode, pk=episode_id,)
    episode.views = episode.views + 1
    episode.save()
    template = 'episode.html'
    context = {
        'title' : episode.title,
        'episode' : episode,
        'episodes' : Episode.objects.filter(publish=True,series=episode.series)

    }
    return render(request, template, context)

def category_page(request,category_id, category_slug):
    category = get_object_or_404(Category, pk=category_id)
    films = Film.objects.filter(publish=True, category=category.title)
    episodes = Episode.objects.filter(publish=True, category=category.title)
    paginator_films = Paginator(films, 25)
    paginator_episodes = Paginator(episodes, 25)
    page = request.GET.get('page')
    try:
        films = paginator_films.page(page)
        episodes = paginator_series.page(page)
    except PageNotAnInteger:
        films = paginator_films.page(1)
        episodes  = paginator_episodes .page(1)
    except EmptyPage:
        films = paginator_films.page(paginator.num_page)
        episodes = paginator_episodes .page(paginator.num_page)

    template = 'category.html'
    context = {
        "category": Category.objects.all(),
        'films': films,
        "episodes": episodes
    }
    return render(request, template, context)

def film_tags(request,tag_slug,tag_id):
    tag = get_object_or_404(FilmTags, pk=tag_id)
    template = 'tags_page.html'
    context = {
        'films': Film.objects.filter(publish=True,tags=tag),
        "tags" : FilmTags.objects.all()
    }
    return render(request, template, context)

def series_tags(request,tag_id):
    tag = get_object_or_404(SeriesTags, pk=tag_id)
    template = 'tags_page.html'
    context = {
        'series1': Series.objects.filter(publish=True, tags=tag),
        "tags": SeriesTags.objects.all()
    }
    return render(request, template, context)





def error_404_view(request, exception):
    return render(request, '404.html')
