from django.urls import path
from . import views
urlpatterns = [
path('home', views.html, name='html'),
path('search', views.search, name='search'),

]
