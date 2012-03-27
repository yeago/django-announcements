from django.dispatch import Signal

announcement_acknowledged = Signal(providing_args=["user"])
