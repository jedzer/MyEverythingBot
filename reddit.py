import requests
import json
import random

memeSubbreddits = [
        "dankmemes",
        "memes",
        "Dark_memes",
        "PewdiepieSubmissions",
        "dank_memes_archive",
        "ProgrammerHumor",
        "tumblr",
        "dank_meme"]


def meme():
    memeSourceToChoose = random.randint(0, len(memeSubbreddits) - 1)
    url = "https://www.reddit.com/r/" + memeSubbreddits[memeSourceToChoose ] + ".json"
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    data = r.json()
    memeToChoose = random.randint(1, data['data']['dist'] - 1)

    print()
    print(url)
    print(data)
    print(memeToChoose)
    return data['data']['children'][memeToChoose]['data']['url']