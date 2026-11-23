#!/usr/bin/env python3

"""Echoing server with asyncio"""

import asyncio
from websockets.asyncio.server import serve

async def handle(websocket):
    while True:
        message = await websocket.recv()
        await websocket.send(message)
        print(message)

async def main():
    server = await serve(handle, "", 8765)
    await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
