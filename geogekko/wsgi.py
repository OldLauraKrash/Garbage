"""
WSGI config for Project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/opt/bitnami/apps/django/django_projects/geogekko')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/geogekko/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "geogekko.production_settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
