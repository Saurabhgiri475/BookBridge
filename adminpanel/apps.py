from django.apps import AppConfig
from django.db.models.signals import post_migrate


def _create_standard_roles(sender, **kwargs):
    from .roles import ensure_roles
    ensure_roles()  # only creates groups that don't exist yet; never overwrites an admin's edits


class AdminpanelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminpanel'

    def ready(self):
        post_migrate.connect(_create_standard_roles, sender=self, dispatch_uid='adminpanel.create_standard_roles')
