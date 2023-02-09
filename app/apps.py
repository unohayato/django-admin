from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    verbose_name = "アプリ" #画面に表示されるアプリケーション名の変更はここでできる
