from django.urls import path, include
from .views import (
    ArticleListView,
)

app_name="BlogApp"
urlpatterns = [
    path(" ", ArticleListView.as_view(), name="Article-list")
]