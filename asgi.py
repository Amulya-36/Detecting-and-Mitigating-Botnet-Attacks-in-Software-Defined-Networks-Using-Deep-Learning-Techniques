"""
ASGI config for detecting_and_mitigating_botnet_attacks.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detecting_and_mitigating_botnet_attacks.settings')

application = get_asgi_application()
