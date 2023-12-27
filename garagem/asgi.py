import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sistema_Garagem_IFRN.settings')

application = get_asgi_application()
