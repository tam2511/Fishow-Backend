from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'space'

    def ready(self):
        import space.signals
