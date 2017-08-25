from django.apps import AppConfig


class UserModelConfig(AppConfig):
    name = 'user_model'

    def ready(self):
        import user_model.signals #imports the singlas


