from django.apps import AppConfig


class GoodsConfig(AppConfig):
    """Конфігурація другого застосунку з товарами."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
