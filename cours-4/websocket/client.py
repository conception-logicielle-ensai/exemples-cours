import asyncio
import websockets

async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Hello, WebSocket Server!"
        print(f"Envoi : {message}")
        await websocket.send(message)

        response = await websocket.recv()
        print(f"Réponse du serveur : {response}")

if __name__ == "__main__":
    asyncio.run(communicate())
