from django.urls import path
from .views import *


app_name = 'social'
urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),
    path('post/<int:pk>', show_post, name="show_post"),
    path('search/', SearchAPI, name='search'),
    path('like/', Like, name='Like-toggle'),
    path('bookmark/', create_bookmark, name='bookmark_create'),
    path('delete/<int:id>', delete, name='delete'),
    path('bookmarks/', bookmark, name='bookmark'),
]
