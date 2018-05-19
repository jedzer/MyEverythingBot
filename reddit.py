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

catsSubReddits = [
        "cats",
        "Kitten",
        "kittens"
]

def meme():
    memeSourceToChoose = random.randint(0, len(memeSubbreddits) - 1)
    url = "https://www.reddit.com/r/" + memeSubbreddits[memeSourceToChoose ] + ".json"
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    data = r.json()
    memeToChoose = random.randint(1, data['data']['dist'] - 1)

    print()
    print("---MEME---")
    print(memeToChoose)
    print(url)
    print()

    # print(data)
    return data['data']['children'][memeToChoose]['data']['url']


def cats():
    catsSourceToChoose = random.randint(0, len(catsSubReddits) - 1)
    url = "https://www.reddit.com/r/" + catsSubReddits[catsSourceToChoose] + ".json"
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    data = r.json()
    catToChoose = random.randint(1, data['data']['dist'] - 1)

    print()
    print("---KITTEN---")
    print(catToChoose)
    print(url)
    print()

    # print(data)
    return data['data']['children'][catToChoose]['data']['url']



def reddit(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + ".json"
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    data = r.json()
    postToChoose = random.randint(1, data['data']['dist'] - 1)

    print()
    print("----REDDIT---")
    print(postToChoose)
    print(url)
    print()

    return [data['data']['children'][postToChoose]['data']['url'], data['data']['children'][postToChoose]['data']['title'], "https://www.reddit.com" + data['data']['children'][postToChoose]['data']['permalink']]
