import asyncio
import websockets

# Ensemble pour stocker les connexions actives
connected_clients = set()

async def broadcast(message):
    for client in connected_clients:
        await client.send(message)

async def handle_client(websocket):
    # Ajoute le client connecté à l'ensemble
    connected_clients.add(websocket)
    print(f"Client connecté. Total clients : {len(connected_clients)}")

    try:
        async for message in websocket:
            print(f"Message reçu : {message}")
            await broadcast(f"Message d'un client : {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client déconnecté.")
    finally:
        # Retire le client de l'ensemble à sa déconnexion
        connected_clients.remove(websocket)
        print(f"Client déconnecté. Total clients : {len(connected_clients)}")

async def main():
    async with websockets.serve(handle_client, "localhost", 8765):
        print("Serveur WebSocket démarré sur ws://localhost:8765")
        await asyncio.Future()  # Garde le serveur actif

if __name__ == "__main__":
    asyncio.run(main())
