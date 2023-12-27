import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sistema_Garagem_IFRN.settings')

application = get_wsgi_application()
