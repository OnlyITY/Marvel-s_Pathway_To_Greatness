import requests

class MarvelAPI:
    def __callapi(self, url, params):
        r = requests.get(url, params, headers={'Accept': 'application/json'})
        return r.text

    def getCharcters(self):
        ts = "35201529"  # TimeStamp should we change this?
        # Move this information to a config ?
        apikey = "83cba64ddb32d65ba2c813bde03c4044"
        md5_hash = "76801623818d7ac2534f4686fa0c13fb"
        params = {'ts': ts, 'apikey': apikey, 'hash': md5_hash}
        return self.__callapi("http://gateway.marvel.com/v1/public/characters", params)


    # Search for name=Hulk then print the response text
    def getCharcterInfo(self, name):
        ts = "35201529"  # TimeStamp should we change this?
        # Move this information to a config ?
        apikey = "83cba64ddb32d65ba2c813bde03c4044"
        md5_hash = "76801623818d7ac2534f4686fa0c13fb"
        params = {'ts': ts, 'apikey': apikey, 'hash': md5_hash, 'name': name}
        return self.__callapi("http://gateway.marvel.com/v1/public/characters", params)


    def getCharacterComics(self, name):
        ts = "35201529"  # TimeStamp should we change this?
        # Move this information to a config ?
        apikey = "83cba64ddb32d65ba2c813bde03c4044"
        md5_hash = "76801623818d7ac2534f4686fa0c13fb"
        params = {'ts': ts, 'apikey': apikey, 'hash': md5_hash}
        return self.__callapi("http://gateway.marvel.com/v1/public/characters/%s/comics" % name, params)

    def getCharacterEvents(self, name):
        ts = "35201529"  # TimeStamp should we change this?
        # Move this information to a config ?
        apikey = "83cba64ddb32d65ba2c813bde03c4044"
        md5_hash = "76801623818d7ac2534f4686fa0c13fb"
        params = {'ts': ts, 'apikey': apikey, 'hash': md5_hash}
        return self.__callapi("http://gateway.marvel.com/v1/public/characters/%s/events" % name, params)

    def getComicIssue(self, issueId):
        ts = "35201529"  # TimeStamp should we change this?
        # Move this information to a config ?
        apikey = "83cba64ddb32d65ba2c813bde03c4044"
        md5_hash = "76801623818d7ac2534f4686fa0c13fb"
        params = {'ts': ts, 'apikey': apikey, 'hash': md5_hash}
        # Change the string for getting an issue
        return self.__callapi("comics?ts=35201529&apikey=83cba64ddb32d65ba2c813bde03c4044&hash=76801623818d7ac2534f4686fa0c13fb" % issueId, params)


