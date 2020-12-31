from django.apps import AppConfig


# CheckoutConfig apps

class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
