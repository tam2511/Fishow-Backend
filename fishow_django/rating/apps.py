from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'rating'

    def ready(self):
        import rating.signals
