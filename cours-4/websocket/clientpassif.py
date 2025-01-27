import asyncio
import websockets

async def wait_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Client connecté et en attente.")
        try:
            while True:
                # Attend un message du serveur
                message = await websocket.recv()
                print(f"Message reçu : {message}")
        except websockets.exceptions.ConnectionClosed:
            print("Connexion fermée par le serveur.")

if __name__ == "__main__":
    asyncio.run(wait_client())
