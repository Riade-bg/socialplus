from django.urls import path
from .views import index, detail, result, vote
from . import views

app_name = "mySite"
urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('<int:pk>/',views.detail.as_view(), name="detail"),
    path('<int:pk>/result/', views.result.as_view(), name="result"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    ]