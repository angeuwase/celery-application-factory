$celery -A celery_worker.celery worker --pool=solo --loglevel=debug

the below was working before i introduced the solo execution pool. afterwards it didnt work and resulted in working outside application context error. 
$ celery -A celery_worker.celery worker --pool=gevent --concurrency=500 --loglevel=debug