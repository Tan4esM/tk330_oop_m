#import requests
#
#r = requests.get('https://httpbin.org/')
#print(r.encoding)
#
#for line in r.iter_lines():
#    print(line)

import os

print(f"Це значення зміної MY_ENV: {os.environ.get('MY_ENV')}")
print(f"Це значення зміної MY_ENV_FROM_FILE: {os.environ.get('MY_ENV_FROM_FILE')}")

from jikanpy import Jikan
jikan = Jikan()

anime = jikan.anime(52991, extension='episodes')
for episode in anime['data']:
    print(f"Епізод №{episode['mal_id']} з назвою: {episode['title']} має рейтинг {episode['score']}")