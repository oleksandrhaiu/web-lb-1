from django.urls import path

from . import views

# Окремий роутер для каталогу,
# щоб зручно підключати його в головному urls.py.
urlpatterns = [
    path('', views.index, name='goods-index'),
]