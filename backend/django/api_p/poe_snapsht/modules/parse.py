import requests
import aiohttp
import asyncio
import base64
import zlib
import json
from lxml.etree import fromstring
from poe_snapsht.modules.PoB_json_to_xml import get_pob_xmls

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
        items = info_items['items']
        info = info_items['character']
    async with session.get(url=url_passives) as resp:
        passives = await resp.json()
    print(f'Character {char[1]} fetched successfuly')
    return {
        'char': char,
        'info': info,
        'items': items,
        'passives': passives,
        'info_items': info_items
    }

async def start_fetch(char_list):
    tasks = []
    async with aiohttp.ClientSession(headers=request_headers) as client:
        for char in char_list:
            tasks.append(get_char(client, char))
        results = await asyncio.gather(*tasks)
    char_xmls = get_pob_xmls([[json.dumps(i.pop('info_items')), json.dumps(i['passives'])] for i in results])
    for char, xml in zip(results, char_xmls):
        char['xml_code'] = _fetch_import_code_from_xml(xml)
        char['stats'] = json.dumps(_fetch_stats(xml.encode('utf-8')))
    return results

def _fetch_import_code_from_xml(xml: str) -> bytes:
    """Encodes and zips a Path Of Building import code.

    :return: Compressed XML build document."""

    compressed_xml = zlib.compress(xml.encode('utf-8'))
    base64_encode = base64.urlsafe_b64encode(compressed_xml)
    return base64_encode.decode('utf-8')

def _fetch_stats(xml: str):
    xml = fromstring(xml)
    stats = {
    'full_dps': xml.find("Build").find("PlayerStat[@stat='FullDPS']").get('value'),
    'chaos_resist': xml.find("Build").find("PlayerStat[@stat='ChaosResist']").get('value'),
    'lightning_resist': xml.find("Build").find("PlayerStat[@stat='LightningResist']").get('value'),
    'cold_resist': xml.find("Build").find("PlayerStat[@stat='ColdResist']").get('value'),
    'fire_resist': xml.find("Build").find("PlayerStat[@stat='FireResist']").get('value'),
    'armour': xml.find("Build").find("PlayerStat[@stat='Armour']").get('value'),
    'evasion': xml.find("Build").find("PlayerStat[@stat='Evasion']").get('value'),
    'energy_shield': xml.find("Build").find("PlayerStat[@stat='EnergyShield']").get('value'),
    'mana': xml.find("Build").find("PlayerStat[@stat='Mana']").get('value'),
    'life': xml.find("Build").find("PlayerStat[@stat='Life']").get('value'),
    'str': xml.find("Build").find("PlayerStat[@stat='Str']").get('value'),
    'dex': xml.find("Build").find("PlayerStat[@stat='Dex']").get('value'),
    'int': xml.find("Build").find("PlayerStat[@stat='Int']").get('value'),
    }
    return stats
