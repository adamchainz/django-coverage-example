import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DEBUG = os.environ.get("DEBUG", "") == "1"

SECRET_KEY = "django-insecure-km@s4&x+k9ocyx$ymr%s@we%3z9_55m_d)hsmg)uug)vzff7)9"

# Dangerous: disable host header validation
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "example.core",
]

ROOT_URLCONF = "example.urls"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
