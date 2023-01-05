from channels.routing import URLRouter
from websocket.routing.default import websocket_path

websockets = URLRouter(websocket_path)
