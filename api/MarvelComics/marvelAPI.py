import requests

class MarvelAPI:
    def __init__(self):
        ts="35201529" # TimeStamp should we change this?
        # Move this information to a config ?
        apikey="83cba64ddb32d65ba2c813bde03c4044"
        md5_hash="76801623818d7ac2534f4686fa0c13fb"
        self.params = {'ts': ts,'apikey': apikey, 'hash': md5_hash}

    def __callapi(self, url):
        r = requests.get(url, self.params, headers={'Accept': 'application/json'})
        return r.text

    # Search for name=Hulk then print the response text
    def getCharcterInfo(self, name):
        #?name=Thor&apikey=5231bb34f7a0b26e79ef5e97430b97d6
        return self.__callapi("https://gateway.marvel.com:443/v1/public/characters/%s" % name)
        # fix link so that in case there's a two worded or more superhero, there needs to be a %20 in the space

    def getCharacterComics(self, name):
        return self.__callapi("https://gateway.marvel.com:443/v1/public/characters/%s/comics" % name)

    def getCharacterEvents(self, name):
        return self.__callapi("https://gateway.marvel.com:443/v1/public/characters/%s/events" % name)

    def getComicIssue(self, issueId):
        # Change the string for getting an issue 
        return self.__callapi("comics?ts=35201529&apikey=83cba64ddb32d65ba2c813bde03c4044&hash=76801623818d7ac2534f4686fa0c13fb" %issueId)
