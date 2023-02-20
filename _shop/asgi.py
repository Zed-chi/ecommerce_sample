import os

# from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_shop.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")
from configurations.asgi import get_asgi_application

application = get_asgi_application()
