import urllib.request
import json
import random

memeSubbreddits = [
        "dankmemes",
        "memes",
        "Dark_memes",
        "PewdiepieSubmissions",
        "dank_memes_archive",
        "Spicy_Memes",
        "ProgrammerHumor",
        "tumblr",
        "dank_meme"]


def meme():
    memeToChoose = random.randint(0, len(memeSubbreddits) - 1)
    url = "https://www.reddit.com/r/" + memeSubbreddits[memeToChoose] + ".json?limit=1"
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        print(data['data']['children'][0]['data']['url'])
        return data['data']['children'][0]['data']['url']

        # file = open("reddit.txt", "w")
        # file.write(data)
        # file.close()


