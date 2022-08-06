import requests
import aiohttp
import asyncio

request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_character_list(account):
    url = f'https://www.pathofexile.com/character-window/get-characters?accountName={account}&realm=pc'

    request = requests.get(url, headers=request_headers)
    if request.status_code != requests.codes.ok:
        raise Exception(f'get_character_list response status code:{request.status_code}')
    return request.json()

async def get_char(session, char):
    payload = {
        'accountName': char[0],
        'realm': 'pc',
        'character': char[1]
    }
    url_info_items = 'https://www.pathofexile.com/character-window/get-items'
    url_passives = f'https://www.pathofexile.com/character-window/get-passive-skills?reqData=0&accountName={char[0]}&realm=pc&character={char[1]}'
    async with session.post(url=url_info_items, data=payload) as resp:
        info_items = await resp.json()
        items = info_items.pop('items')
        info = info_items.pop('character')
    async with session.get(url=url_passives) as resp:
        passives = await resp.json()
    print(f'Character {char[1]} fetched successfuly')
    return (char, info, items, passives)

async def start_fetch(char_list):
    tasks = []
    async with aiohttp.ClientSession(headers=request_headers) as client:
        for char in char_list:
            tasks.append(get_char(client, char))
        results = await asyncio.gather(*tasks)
    return results
