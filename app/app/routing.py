from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, ChannelNameRouter
from django.core.asgi import get_asgi_application

from websocket.routing import websockets

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(websockets),
})
