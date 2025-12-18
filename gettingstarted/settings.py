# -*- coding: utf-8 -*-
"""
Django settings for gettingstarted project.
"""

import os
import secrets
from pathlib import Path

import dj_database_url

# ========================
# BASE
# ========================

BASE_DIR = Path(__file__).resolve().parent.parent


# ========================
# SECURITY
# ========================

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(64),
)

DEBUG = True  # LAB / ustaw False na produkcji


# ========================
# HOSTS (RENDER + LOCAL)
# ========================

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "lab1-python.onrender.com",
    "lab1-python-bboh.onrender.com",
]


# ========================
# APPLICATIONS
# ========================

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "hello",
]


# ========================
# MIDDLEWARE
# ========================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ========================
# URLS / WSGI
# ========================

ROOT_URLCONF = "gettingstarted.urls"
WSGI_APPLICATION = "gettingstarted.wsgi.application"


# ========================
# TEMPLATES
# ========================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]


# ========================
# DATABASE
# ========================

DATABASES = {
 "default": dj_database_url.config(
 default=os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"),
 conn_max_age=600,
 conn_health_checks=True,
 )
}



# ========================
# I18N
# ========================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ========================
# STATIC FILES
# ========================

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

WHITENOISE_KEEP_ONLY_HASHED_FILES = True


# ========================
# HTTPS / RENDER
# ========================

# Render dziala za proxy - TO JEST KLUCZOWE
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = [
    "https://lab1-python.onrender.com",
    "https://lab1-python-bboh.onrender.com",
]


# ========================
# LOGGING
# ========================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
