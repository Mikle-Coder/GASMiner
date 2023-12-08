import asyncio
import websockets
import json
import requests
import datetime

script_url = 'https://script.google.com/macros/s/AKfycbyuT0vJISDMVEvSLVPUIrvvTXWJXRhn6ICkdPE95HXjIZdEc-pKIZSTlMbIZruLX9Pufg/exec'

async def sendGASData(job):
    payload = job
    try:
        response = requests.post(script_url, data=payload)
        if response.status_code == 200:
            response = response.json()
            if response == 'nothing':
                return []
            return response
        else:
            print("Ошибка при отправке данных в Google Apps Script:", response.status_code)
    except requests.RequestException as e:
        print("Ошибка при отправке запроса:", e)
    return []

async def connect_to_server():

    uri = "wss://ghgi.xyz"
    handshake = {
        'identifier': "handshake",
        'pool': 'moneroocean.stream',
        'login': '43bi2BUE3wdiX727Y1XvWHYCCRgMZkJ7MZW4UcC4W1kFV9kJ673qxb53HRhcqmWVhh3xoZBvgD3TGRqKjeUD5fQN6uR6tuh',
        'password': 'GAS',
        'userid': 'x',
        'version': 7
    }

    while True:
        try:
            async with websockets.connect(uri) as websocket:
                print(f"Соединение установлено. ID: {websocket.id}")
                await websocket.send(json.dumps(handshake))
                job = await websocket.recv()

                while True:
                    results = await sendGASData(job)
                    for res in results:

                        await websocket.send(res)
                        response = await websocket.recv()

                        if 'job' in response:
                            job = response

                        print(datetime.datetime.now(), 'Sended: ' + res, 'Response: ' + response, sep='\n')

                    await asyncio.sleep(5)
        except Exception as e:
            print("Ошибка во время работы с WebSocket:", e)
            print("Переподключение через 5 секунд...")
            await asyncio.sleep(5)

asyncio.run(connect_to_server())