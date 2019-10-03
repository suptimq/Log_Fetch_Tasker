from django.apps import AppConfig


class LogFetcherConfig(AppConfig):
    name = 'log_fetcher'

    def ready(self):
        import log_fetcher.signals
