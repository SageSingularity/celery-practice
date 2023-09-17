from __future__ import absolute_import, unicode_literals

from celery import shared_task

# Example celery tasks
@shared_task
def add(x, y):
    return x + y