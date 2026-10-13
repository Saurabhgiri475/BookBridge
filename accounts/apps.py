from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from django.contrib.auth.signals import user_logged_in

        from . import twofactor

        def forget_2fa_on_login(sender, request, user, **kwargs):
            # Every new login starts unverified, even if the session was reused.
            if request is not None and hasattr(request, 'session'):
                twofactor.clear_verified(request)

        user_logged_in.connect(forget_2fa_on_login, dispatch_uid='accounts.forget_2fa_on_login')
