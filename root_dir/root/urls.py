
from django.contrib import admin
from django.urls import path, include
from social.views import profile
from imessage.views import messanger_home, messanger_create, messanger_show
urlpatterns = [
    path('', include('users.urls')),
    path('profile/<str:slug>/', profile, name="profile"),
    path('imessage/', messanger_home, name="messenger"),
    path('send_imessage/', messanger_create, name="messanger_create"),
    path('chat/', messanger_show, name="messanger_create"),
    path('home/', include('social.urls'), name="home"),
    path('admin/', admin.site.urls),
]
