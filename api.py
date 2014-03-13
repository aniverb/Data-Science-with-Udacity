import json
import requests

def api_get_request(url):
    if __name__=="__main__":
        data=requests.get(url).text
        data=json.loads(data)
        a=data['topartists']["artist"]
        b=[]
        for i in a:
            b.append(i['name'])   
    return b   
    # call the last.fm API to get a list of the
    # top artists in Spain and return the name of the number 1 top artist in Spain.
    
api_get_request('http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks&country=nigeria&api_key=f4d7199cde85ab82b5badfaf4f142073&format=json') 

b=[]
for i in a:
    b.append(i['name'])
    
c=[]
for i in a:    
    c.append(i["listeners"])
    
def api_get_request2(url):
    if __name__=="__main__":
        data=requests.get(url).text
        data=json.loads(data)
    return data['topartists']["artist"][0]['name']
       
api_get_request2('http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=f4d7199cde85ab82b5badfaf4f142073&format=json')    
    
data.describe()
