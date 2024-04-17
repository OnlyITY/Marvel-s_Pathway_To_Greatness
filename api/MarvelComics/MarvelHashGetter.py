#importing dependencies
import time


privKey = "a4aeb5fe56bc287c1e054fbeab78e4e775a28c83"
pubKey = "5231bb34f7a0b26e79ef5e97430b97d6"


def getHash():
    ts = str(time.time()) #Creates a time stamp
    hasht = ts + privKey + pubKey

    return ts, hasht

