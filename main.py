import requests
import bs4

def get_gif(query):
    li = []
    res = requests.get(f"https://tenor.com/search/{query}-gifs")

    res = bs4.BeautifulSoup(res.text,"html.parser")
    res = res.find_all("div", {"class": "Gif"})
    #print(res[2]["href"])
    for x in res:
        nres = bs4.BeautifulSoup(str(x),"html.parser")
        nres = nres.find_all(name="img")
        li.append(nres[0]["src"])
    return li 

def get_sticker(query):
    li = []
    res = requests.get(f"https://tenor.com/search/{query}-gifs")

    res = bs4.BeautifulSoup(res.text,"html.parser")
    res = res.find_all("div", {"class": "Sticker"})
    #print(res[2]["href"])
    for x in res:
        nres = bs4.BeautifulSoup(str(x),"html.parser")
        nres = nres.find_all(name="img")
        li.append(nres[0]["src"])
    return li 

print(get_gif("lol"))
print(get_sticker("lol"))
