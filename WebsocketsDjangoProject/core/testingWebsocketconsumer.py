import asyncio
import websockets

async def test():
    uri = "ws://127.0.0.1:8000/ws/chat/test/"  # Update to your Channels route
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from Python CLI!")
        reply = await websocket.recv()
        print("Reply from server:", reply)

asyncio.run(test())
