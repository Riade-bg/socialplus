from django.urls import path
from website.views import product, show

app_name="website"
urlpatterns = [
    path('', product),
    path('<int:id>/', show, name="Product"),
    # path('product/<int:id>/delete', delete),
    # path('create/', create_product),
]
