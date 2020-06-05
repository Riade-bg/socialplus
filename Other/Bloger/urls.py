from django.urls import path
from .views import PostListView, PostDetailView, PostCreatelView, PostUpdatelView, PostDeletelView
from django.contrib.auth import views as auth_views

app_name = 'Bloger'
urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('<int:pk>/', PostDetailView.as_view(), name="detail-post"),
    path('<int:pk>/update', PostUpdatelView.as_view(), name="update-post"),
    path('<int:pk>/delete', PostDeletelView.as_view(), name="delete-post"),
    path('post/new/', PostCreatelView.as_view(), name="create-post"),
    path('passwordreset/', auth_views.PasswordResetView.as_view(template_name="passwordReset.html"), name="password_reset"),
    # path('passwordreset/done/', auth_views.PasswordResetDoneView.as_view(template_name="passwordResetDone.html"), name="password_reset_done"),
    path('passwordreset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="passwordResetConfirm.html"), name="password_reset_done"),
]