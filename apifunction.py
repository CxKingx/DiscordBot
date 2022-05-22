import requests
# https://waifu.pics/docs


class WaifuPic:
    def __init__(self):
        pass

    def fetchanimuneko(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/nsfw/neko")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimubonk(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/bonk")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content  
    
    def fetchanimushinobu(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/shinobu")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content   
    def fetchanimuyeet(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/yeet")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content 
    
    def fetchanimutrap(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/nsfw/trap")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content 
    def fetchanimucry(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/cry")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content  
    def fetchanimupat(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://some-random-api.ml/animu/pat")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimukiss(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://anime-api.hisoka17.repl.co/img/kiss")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimucuddle(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://anime-api.hisoka17.repl.co/img/cuddle")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimupunch(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://anime-api.hisoka17.repl.co/img/punch")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content  
    
    def fetchanimuslap(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://anime-api.hisoka17.repl.co/img/slap")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimuboob(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://anime-api.hisoka17.repl.co/img/nsfw/boobs")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimuhentai(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://anime-api.hisoka17.repl.co/img/nsfw/hentai")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content

    def fetchanimuhug(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://some-random-api.ml/animu/hug")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    
    def fetchanimuquote(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://some-random-api.ml/animu/quote")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content

    def fetchanimuwaifunsfw(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/nsfw/waifu")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    def fetchanimumegumin(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/megumin")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content
    def fetchanimunekosfw(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/neko")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content  
    def fetchanimuhi5(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/highfive")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content

    def fetchanimubite(self):
        #making a GET request to the endpoint.
        resp = requests.get("https://api.waifu.pics/sfw/bite")
        #checking if resp has a healthy status code.
        if 300 > resp.status_code >= 200:
            content = resp.json() #We have a dict now.
        else:
            content = f"Recieved a bad status code of {resp.status_code}."
        #print(content)
        return content

