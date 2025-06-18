from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({
            "message": "WebSocket connected successfully!"
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '')

        # Echo the message back
        await self.send(text_data=json.dumps({
            "message": f"Server received: {message}"
        }))

    async def disconnect(self, close_code):
        print(f"WebSocket closed with code: {close_code}")
