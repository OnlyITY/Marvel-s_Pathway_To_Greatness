#importing dependencies
import hashlib
import time
import json
import requests

def getHash():
    privKey = "a4aeb5fe56bc287c1e054fbeab78e4e775a28c83"
    pubKey = "5231bb34f7a0b26e79ef5e97430b97d6"
    getMd5 = hashlib.md5()

    ts = str(time.time()) #Creates a time stamp
    ts_byte = bytes(ts, 'utf-8') #Turns the time stamp into a byte
    m.update(ts_byte)
    m.uodate(b"a4aeb5fe56bc287c1e054fbeab78e4e775a28c83") #add private key
    m.update(b"5231bb34f7a0b26e79ef5e97430b97d6") #add public key

    hasht = m.hexdigest()

    return ts, hasht

