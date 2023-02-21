import os
from pathlib import Path

from configurations import Configuration, values
from environs import Env

env = Env()
env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


class Dev(Configuration):
    DOTENV = os.path.join(BASE_DIR, ".env")
    SECRET_KEY = (
        "django-insecure-$hl^e%q-y6vrl29w7jdshquikf8-n-y&a%dfsduxu-bd3-!sp$"
    )
    DEBUG = True
    ALLOWED_HOSTS = ["*"]

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "main",
        "products",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "_shop.urls"
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [
                (BASE_DIR / "templates"),
            ],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "_shop.wsgi.application"

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]

    LANGUAGE_CODE = "ru"
    TIME_ZONE = "Europe/Moscow"
    USE_I18N = True
    USE_TZ = True

    STATIC_URL = "static/"
    STATIC_ROOT = BASE_DIR
    STATICFILES_DIRS = [BASE_DIR / "./static"]
    MEDIA_URL = "media/"
    MEDIA_ROOT = BASE_DIR / "media/"

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


class Prod(Dev):
    SECRET_KEY = env.str("DJANGO_SECRET_KEY")
    DEBUG = env.bool("DEBUG")
    ALLOWED_HOSTS = []
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
    STATICFILES_DIRS = [BASE_DIR / env.str("STATIC_ROOT")]
    MEDIA_ROOT = BASE_DIR / env.str("MEDIA_ROOT")
