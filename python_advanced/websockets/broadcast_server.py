#!/usr/bin/env python3

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

CONNECTED_CLIENTS = set()


async def handle(websocket):
    CONNECTED_CLIENTS.add(websocket)
    print(CONNECTED_CLIENTS)

    try:
        async for message in websocket:
            for client in CONNECTED_CLIENTS:
                await client.send(f"B:{message}")
    except ConnectionClosed:
        print(f"Disconnected Client {websocket}")
    finally:
        CONNECTED_CLIENTS.remove(websocket)


async def main():
    server = await serve(handle, "", 8765)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
