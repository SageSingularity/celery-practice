# Table of Contents
* [Summary](#summary)
* [When is Celery Needed?](#when-is-celery-needed)
* [Tools Used in this Repo](#tools-used-in-this-repo)
* [Sources of Information on Celery](#sources-of-information-on-celery)

# Summary
A practice repo for the Celery Tool.

# When is Celery Needed?
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

# Tools Used in this Repo
* [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
* [Django](https://www.djangoproject.com/)
* [RabbitMQ](https://www.rabbitmq.com/)

# Sources of Information on Celery
The following are useful sources of information on Celery. This may include the docs, Youtube videos, Newsletter Articles, etc.
* [Celery Docs](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
* [Learn Django & Celery with RabbitMQ - Youtube Tutorials by Very Academy](https://youtu.be/fBfzE0yk97k?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20
