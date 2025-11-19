from django.urls import path

from . import views

# Окремий файл маршрутів робить застосунок незалежним.
# Тут описую лише те, що стосується магазину.
urlpatterns = [
    path('', views.index, name='shop-index'),
]
