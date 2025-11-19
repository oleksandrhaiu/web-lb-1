from django.apps import AppConfig


class ShopConfig(AppConfig):
    """
    Базова конфігурація застосунку.
    Django автоматично прочитає її, коли я додам 'shop' до INSTALLED_APPS.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
