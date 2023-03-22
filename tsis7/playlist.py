import requests
from dotenv import load_dotenv
import os
import base64
import json

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
playlist_id = os.getenv('PLAYLIST_ID')
BASEURL = 'https://api.spotify.com/v1'


def get_token():
    auth_string = f'{client_id}:{client_secret}'
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-type': 'application/x-www-form-urlencoded'
    }

    data = {'grant_type': 'client_credentials'}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token


def get_auth_header(token):
    return {'Authorization': f'Bearer {token}'}


def search_spotify(token, search):
    headers = get_auth_header(token)
    query = f'?q={search}&type=artist,track&limit=1'

    query_url = f'{BASEURL}/search{query}'
    result = requests.get(query_url, headers=headers)

    json_result = json.loads(result.content)
    return json_result


def get_playlist(token, playlist_id):
    headers = get_auth_header(token)
    query='?limit=1'
    result = requests.get(f'{BASEURL}/playlists/{playlist_id}/tracks{query}', headers=headers)

    json_result = json.loads(result.content)['items']
    return json_result


token = get_token()
songs = get_playlist(token, playlist_id)
#print(songs)
for idx, song in enumerate(songs):
    print(song['track'])
    #print(f"{idx + 1}. {song['track']['name']} : {song['track']['']}")
