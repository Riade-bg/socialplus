"""Projects URL Configuration

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
from django.contrib          import admin
from django.urls             import path, include
from django.contrib.auth     import views as auth_views
from users.views             import profile, register
from django.conf             import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register, name="register"),
    path('Blog/', include('Bloger.urls')),
    path('admin/', admin.site.urls),
    path('profile/', profile, name="profile"),
    path('', auth_views.LoginView.as_view(template_name="login.html", redirect_authenticated_user=True), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout")
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
