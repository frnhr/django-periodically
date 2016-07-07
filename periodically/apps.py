from __future__ import \
    unicode_literals, print_function, division, absolute_import

from django.apps import AppConfig

from periodically import autodiscover
from . import settings

class PeriodicallyConfig(AppConfig):
    name = 'periodically'

    def ready(self):
        if settings.AUTODISCOVER:
            autodiscover()
