celery -A pizzeria.celery beat -l info
celery -A pizzeria.celery worker --pool=solo -l info
