import requests
import aiohttp
import asyncio
import base64
import zlib
import json
from PoB_json_to_xml import get_pob_xmls
# import pobapi

request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_character_list(account):
    url = f'https://www.pathofexile.com/character-window/get-characters?accountName={account}&realm=pc'

    request = requests.get(url, headers=request_headers)
    if request.status_code != requests.codes.ok:
        return request.status_code
    return request.json()

async def get_char(session, char) -> tuple:
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
    return (char, info, items, passives, info_items)

async def start_fetch(char_list):
    tasks = []
    async with aiohttp.ClientSession(headers=request_headers) as client:
        for char in char_list:
            tasks.append(get_char(client, char))
        results = await asyncio.gather(*tasks)
    char_xmls = get_pob_xmls([[json.dumps(i[3]), json.dumps(i.pop(4))] for i in results])
    for char, xml in zip(results, char_xmls):
        char[4] = _fetch_import_code_from_xml(xml)
    return results

def _fetch_import_code_from_xml(xml: str) -> bytes:
    """Encodes and zips a Path Of Building import code.

    :return: Compressed XML build document."""

    base64_encode = base64.urlsafe_b64encode(xml)
    compressed_xml = zlib.compress(base64_encode)
    return compressed_xml