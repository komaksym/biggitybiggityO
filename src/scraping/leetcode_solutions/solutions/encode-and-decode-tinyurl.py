# Time:  O(1)

import random


class Codec(object):
    def __init__(self):
        self.__random_length = 6
        self.__tiny_url = "http://tinyurl.com/"
        self.__alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__lookup = {}

    def encode(self, longUrl):
        def getRand():
            rand = []
            for _ in range(self.__random_length):
                rand += self.__alphabet[random.randint(0, len(self.__alphabet)-1)]
            return "".join(rand)

        key = getRand()
        while key in self.__lookup:
            key = getRand()
        self.__lookup[key] = longUrl
        return self.__tiny_url + key

    def decode(self, shortUrl):
        return self.__lookup[shortUrl[len(self.__tiny_url):]]


from hashlib import sha256


class Codec2(object):

    def __init__(self):
        self._cache = {}
        self.url = 'http://tinyurl.com/'

    def encode(self, long_url):
        key = sha256(long_url.encode()).hexdigest()[:6]
        self._cache[key] = long_url
        return self.url + key

    def decode(self, short_url):
        key = short_url.replace(self.url, '')
        return self._cache[key]


