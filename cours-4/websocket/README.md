# Websockets

petit exemple de websocket avec client et serveur en python
## How to run it

Il faut ici lancer le websocket parallelement aux clients
```
pip install -r cours-4/websocket/requirements.txt
python3 cours-4/websocket/server.py
```

Dans un autre terminal
```
python3 cours-4/websocket/clientpassif.py
```

> Ce programme se connecte au websocket et écoute ce qu'il broadcaste

Et dans un terminal "client", on va pouvoir requêter le websocket

Ouvrir un autre terminal :
```
python3 cours-4/websocket/client.py
```

> Il y a également un client html, vous pouvez y accéder en utilisant votre navigateur.
