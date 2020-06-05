from django.urls import path
from .views import index, add_todo, delete

app_name = 'todo'
urlpatterns = [
    path('', index, name="index"),
    path('add_todo/', add_todo, name="add_todo"),
    path('delete/<int:id>/', delete, name="delete"),
]