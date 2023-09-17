from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_with_celery.settings')

# The Celery Instance, which we configure and then run
app = Celery('django_with_celery')

# Celery configuration
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically find tasks and import into Celery
app.autodiscover_tasks()