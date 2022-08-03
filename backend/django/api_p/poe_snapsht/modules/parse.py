import requests
from urllib.parse import quote


request_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def get_character_list(account):
    url = f'https://www.pathofexile.com/character-window/get-characters?accountName={account}&realm=pc'

    request = requests.get(url, headers=request_headers)
    if request.status_code != requests.codes.ok:
        raise Exception(f'get_character_list response status code:{request.status_code}')
    return request.json()

def get_character_items(account, char):
    url = 'https://www.pathofexile.com/character-window/get-items'
    payload = {
        'accountName': account,
        'realm': 'pc',
        'character': char
    }
    request = requests.post(url, payload, headers=request_headers)
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