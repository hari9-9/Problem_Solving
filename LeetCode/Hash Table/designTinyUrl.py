class Codec:

    def __init__(self):
        self.hash = {}
        self.idx = 0
        self.domain = "https://tinyurm.com/"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.idx+=1
        self.hash[str(self.idx)] = longUrl
        return f'{self.domain}{self.idx}'


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idx = shortUrl.split('/')[-1]
        return self.hash[idx]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
