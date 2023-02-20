import os

# from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_shop.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")
from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
