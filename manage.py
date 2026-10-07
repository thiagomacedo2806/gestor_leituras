import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        DEBUG=True,
        SECRET_KEY="segredo-super-secreto-para-leituras",
        ROOT_URLCONF=__name__,
        INSTALLED_APPS=[
            "django.contrib.contenttypes",
            "django.contrib.auth",
            "leituras",
        ],
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": "db_leituras.sqlite3",
            }
        },
        MIDDLEWARE=[
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
        ],
    )

from django.urls import path
from leituras import listar_leituras, criar_leitura

urlpatterns = [
    path("", listar_leituras, name="listar"),
    path("criar/", criar_leitura, name="criar"),
]

if __name__ == "__main__":
    execute_from_command_line(sys.argv)