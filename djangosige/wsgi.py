"""
WSGI config for djangosige project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from  dj_static import Cling
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")))
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../")))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangosige.configs.settings")

application = Cling(get_wsgi_application())
