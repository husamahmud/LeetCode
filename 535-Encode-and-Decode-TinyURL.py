class Codec:
    def __init__(self):
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        key = str(len(self.url_map))
        self.url_map[key] = longUrl
        return key

    def decode(self, shortUrl: str) -> str:
        return self.url_map.get(shortUrl)