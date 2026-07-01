"""
WSGI config for barbsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'barbsite.settings')

# get_wsgi_application() calls django.setup(), which populates the app
# registry. It must run before call_command(), otherwise management
# commands fail with AppRegistryNotReady.
application = get_wsgi_application()

# On Vercel, the app runs in a serverless environment and the SQLite database
# may need to be initialized on cold start. Running migrations here ensures the
# booking table exists before any POST request attempts to write to it.
# Also collect static files on first run.
if os.environ.get('VERCEL') or os.environ.get('VERCEL_ENV') or os.environ.get('VERCEL_URL'):
    try:
        from django.core.management import call_command
        call_command('migrate', '--noinput')
        call_command('collectstatic', '--noinput')
    except Exception:
        import traceback
        traceback.print_exc()
