from django.contrib import admin
from django.urls import path
from page import views
from page.views import home, film_page,series_page,episode_page,error_404_view,film_tags,series_tags,search,category_page
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('s/',search,name='search'),
    path('category/<int:category_id>/<str:category_slug>',category_page,name='category'),
    path('tags/<int:tag_id>/<str:tag_slug>',film_tags,name='tags_film'),
    path('tags/<int:tag_id>',series_tags,name='tags_series'),
    path('film/<int:film_id>/<str:film_slug>', film_page, name='film'),
    path('series/<int:series_id>/<str:series_slug>', series_page, name='series'),
    path('series/<str:episode_slug>/episode/<int:episode_id>', episode_page, name='episode'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'page.views.error_404_view'