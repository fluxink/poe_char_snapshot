import requests
from urllib.parse import quote

payload = {
    'accountName': 'Fluxink',
    'realm': 'pc',
    'character': 'Холодный_яр'
}

request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

items_url = 'https://www.pathofexile.com/character-window/get-items'
passive_skills_url = 'https://www.pathofexile.com/character-window/get-passive-skills?reqData=0&accountName=Fluxink&realm=pc&character='

def get_character_list(account):
    url = 'https://www.pathofexile.com/character-window/get-characters'
    payload = {
        'accountName': account,
        'realm': 'pc'
    }
    request = requests.post(url, payload, headers=request_headers)
    if request.status_code != requests.codes.ok:
        raise Exception(f'get_character_list response status code:{request.status_code}')
    return request.json()

def get_character_items(account, char):
    payload = {
        'accountName': account,
        'realm': 'pc',
        'character': char
    }
    request = requests.post(items_url, payload, headers=request_headers)
    if request.status_code != requests.codes.ok:
        raise Exception(f'get_character_items response status code:{request.status_code}')
    return request.json()

def get_character_passives(account, char):
    char = quote(char)
    url = f'https://www.pathofexile.com/character-window/get-passive-skills?reqData=0&accountName={account}&realm=pc&character={char}'
    request = requests.get(url, headers=request_headers)
    if request.status_code != requests.codes.ok:
        raise Exception(f'get_character_passives response status code:{request.status_code}')
    return request.json()