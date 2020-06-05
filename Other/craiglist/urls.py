from django.urls import path
from . import views
from .views import index

app_name = "craiglist"
urlpatterns = [
    path('', views.index, name="index"),
    path('newSearch/', views.new_search, name="new_search"),
    ]