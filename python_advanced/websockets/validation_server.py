#!/usr/bin/env python3

"""Validating inputs for correct input"""

import asyncio
from websockets.exceptions import ConnectionClosed
from websockets.asyncio.server import serve


async def handler(websocket):
    while True:
        try:
            message = await websocket.recv()
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send(f"OK:{message}")
            print(message)
        except ConnectionClosed:
            print("Closed Connection")
            return


async def main():
    server = await serve(handler, "", 8765)
    await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
