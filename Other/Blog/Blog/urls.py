"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BlogApp.views import ArticleListView, DetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from course.views import CourseView

urlpatterns = [
    path('', ArticleListView.as_view(), name="Article-list"),
    path('create/', ArticleCreateView.as_view(), name="Article-create"),
    path('<int:id>/', DetailView, name="Article-detail"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="Article-update"),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name="Article-delete"),
    path('admin/', admin.site.urls),

    path('main', CourseView.as_view(template_name="about.html"), name="course-list"),


]
