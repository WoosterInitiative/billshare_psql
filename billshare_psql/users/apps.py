from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "billshare_psql.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import billshare_psql.users.signals  # noqa F401
        except ImportError:
            pass
