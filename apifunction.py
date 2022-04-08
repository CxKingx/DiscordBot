import requests
# https://waifu.pics/docs
def fetchanimuneko():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/nsfw/neko")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimubonk():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/bonk")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content  
  
def fetchanimushinobu():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/shinobu")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content   
def fetchanimuyeet():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/yeet")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content 
  
def fetchanimutrap():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/nsfw/trap")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content 
def fetchanimucry():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/cry")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content  
def fetchanimupat():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animu/pat")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimukiss():
    #making a GET request to the endpoint.
    resp = requests.get("https://anime-api.hisoka17.repl.co/img/kiss")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimucuddle():
    #making a GET request to the endpoint.
    resp = requests.get("https://anime-api.hisoka17.repl.co/img/cuddle")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimupunch():
    #making a GET request to the endpoint.
    resp = requests.get("https://anime-api.hisoka17.repl.co/img/punch")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content  
  
def fetchanimuslap():
    #making a GET request to the endpoint.
    resp = requests.get("https://anime-api.hisoka17.repl.co/img/slap")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimuboob():
    #making a GET request to the endpoint.
    resp = requests.get("https://anime-api.hisoka17.repl.co/img/nsfw/boobs")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimuhentai():
    #making a GET request to the endpoint.
    resp = requests.get("https://anime-api.hisoka17.repl.co/img/nsfw/hentai")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content

def fetchanimuhug():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animu/hug")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
  
def fetchanimuquote():
    #making a GET request to the endpoint.
    resp = requests.get("https://some-random-api.ml/animu/quote")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content

def fetchanimuwaifunsfw():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/nsfw/waifu")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
def fetchanimumegumin():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/megumin")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content
def fetchanimunekosfw():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/neko")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content  
def fetchanimuhi5():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/highfive")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content

def fetchanimubite():
    #making a GET request to the endpoint.
    resp = requests.get("https://api.waifu.pics/sfw/bite")
    #checking if resp has a healthy status code.
    if 300 > resp.status_code >= 200:
        content = resp.json() #We have a dict now.
    else:
        content = f"Recieved a bad status code of {resp.status_code}."
    #print(content)
    return content

