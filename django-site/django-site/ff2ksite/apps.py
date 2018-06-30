from django.apps import AppConfig


class Ff2KsiteConfig(AppConfig):
    name = 'ff2ksite'

    def ready(self):
        import ff2ksite.signals