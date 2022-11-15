from django.urls import path
from . import views
urlpatterns = [
path('home', views.html, name='html'),
path('image', views.image, name='image'),

path('search', views.search, name='search'),
path('image/search', views.searchdata, name='searchdata'),
path('web/scrape', views.webscrape, name='webscrape'),
path('find/image/url', views.findimg, name='findimg'),


]
