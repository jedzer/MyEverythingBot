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
    meme = getPostJSON(memeSubbreddits[memeSourceToChoose])
    print("\n---MEME---")
    print(memeSubbreddits[memeSourceToChoose])
    print(meme['data']['url'])
    return meme['data']['url']


def cats():
    catsSourceToChoose = random.randint(0, len(catsSubReddits) - 1)
    catPostJSON = getPostJSON(catsSubReddits[catsSourceToChoose])
    print("\n---KITTEN---")
    print(catsSubReddits[catsSourceToChoose])
    print(catPostJSON['data']['url'])
    return catPostJSON['data']['url']


def getPostJSON(subreddit):
    url = "https://www.reddit.com/r/" + subreddit + ".json"
    r = requests.get(url, headers={'User-agent': 'your bot 0.1'})
    data = r.json()
    if 'error' in data:
        return "ERROR"
    if data['data']['dist'] == 1:
        return "ERROR"
    else:
        postToChoose = random.randint(1, data['data']['dist'] - 1)
    return data['data']['children'][postToChoose]


def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif")
   r = requests.head(image_url)
   if r.headers["content-type"] in image_formats:
      return True
   return False


def reddit(subreddit):
    post = getPostJSON(subreddit)
    print("\n----REDDIT---")
    if post == "ERROR":
        return post
    imgUrl = post['data']['url']
    if is_url_image(imgUrl):
        title = post['data']['title']
        if len(title) > 50:
            title = title[0:50]
        return [
                    post['data']['url'],
                    title + "...",
                    "https://www.reddit.com" + post['data']['permalink']
                ]
    else:
        return ["NOTANIMAGE", post['data']['title'], "https://www.reddit.com" + post['data']['permalink']]