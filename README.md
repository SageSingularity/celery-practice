# Table of Contents
* [Summary](#summary)
* [Tools Used in this Repo](#tools-used-in-this-repo)
* [Q&A](#qa)
  * [How do I start Celery?](#how-do-i-start-celery)
  * [When is Celery Needed?](#when-is-celery-needed)
  * [How does a Tool like Django Work with Celery](#how-does-a-tool-like-django-work-with-celery)
* [Sources of Information on Celery](#sources-of-information-on-celery)

# Summary
A practice repo for the Celery Tool.

# Q&A
Various questions that came up during my exploration of Celery, and their answers.

## How do I start Celery?
First, ensure RabbitMQ has been started on the system (dev environment or Docker container).

In the Terminal, specify the Django main project directory using Celery:
* `celery -A django_with_celery worker -l info`

Note that RabbitMQ is automatically select; Redis may take different steps.

The `autodiscover` Celery option is used within `celery.py`, which means tasks will be
dynamically included.

When you execute the above command, you should receive a large amount of informational
output from Celery; it should identify the Tasks and reference `django_with_celery`.

## How do I run a Task manually in Celery?
Use Django Shell to test Celery Tasks.
* `python3 manage.py shell`

Import the Celery Tasks inside the Shell:
* `from celery_app.tasks import *`

You have two options for running Tasks in Celery:
* `delay`
* `apply_async`

Example:
* `<task>.delay(<task_arguments>)`
* `<task>.apply_async((<task_arguments_inside_tuple>), countdown=<time_until_task_starts>)`
* `add.delay(4,4)`
* `add.apply_async((4,4), countdown=5)`

If you head over to your Worker, you should see the task arrive, be processed, and the result
output. In the case of `add.delay(4,4)` the result is `8`, because `4 + 4`.

## When is Celery Needed?
* **When server resources are limited**
* **When a Task Queue / Process manager is needed**
* **When processes need to be executed on demand / periodically**
* **When workloads need to be distributed**
* Examples:
  * Especially helpful in Django, to avoid 'waiting' on the HTTP Request & Response cycle
  * Offloading heavy tasks to a separate thread
  * Processing Queries
  * Processing Data
  * Ancillary tasks, such as creating Reports, ML Video/Image Processing, Large Datasets etc.

## How does a Tool like Django Work with Celery?
* **Django -> Task Messages -> Message**
  *  Using RabbitMQ: **Django -> RabbitMQ -> Celery**
  *  Using Redis: **Django -> Redis -> Celery**
* [Django Finite State Machine](https://github.com/viewflow/django-fsm) can also be used with Celery to make things more maintainable

## Where in Django is Celery Implemented?
* `celery.py`: Is where the instance of Celery is initialized, along with configuration
* `/celery_app`: Django App that implements Celery Tasks
  * `tasks.py`: Where Celery Tasks are defined

# Tools Used in this Repo
* [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
* [Django](https://www.djangoproject.com/)
* [RabbitMQ](https://www.rabbitmq.com/) (Could also use [Redis](https://redis.io/))
* [venv](https://docs.python.org/3/library/venv.html) (Python Virtual Environment, see `/venv`)
* A possible helpful additional tool: [Django Finite State Machine](https://github.com/viewflow/django-fsm)

# Sources of Information on Celery
The following are useful sources of information on Celery. This may include the docs, Youtube videos, Newsletter Articles, etc.
* [Celery Docs](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
* [Learn Django & Celery with RabbitMQ - Youtube Tutorials by Very Academy](https://youtu.be/fBfzE0yk97k?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20
