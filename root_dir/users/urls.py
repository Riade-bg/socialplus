from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import *
from .forms import CustomAuthForm
from django.conf import settings
from django.conf.urls.static import static

app_name="users"
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name="users/home.html", redirect_authenticated_user=True, authentication_form=CustomAuthForm), name="home"),
    path('register/', register, name="register"),
    path('settings/', setting, name="settings"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
