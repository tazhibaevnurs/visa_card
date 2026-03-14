"""
Vercel serverless entry point.
Exposes Django WSGI app as `app` for Vercel Python runtime.
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VisaCard.settings')

# На Vercel при первом запуске выполняем миграции (БД в /tmp создаётся в рантайме).
if os.environ.get('VERCEL'):
    import django
    django.setup()
    from django.core.management import call_command
    from django.conf import settings
    if settings.DATABASES.get('default', {}).get('NAME') == '/tmp/db.sqlite3':
        try:
            call_command('migrate', '--noinput')
        except Exception:
            pass

from VisaCard.wsgi import application

app = application
