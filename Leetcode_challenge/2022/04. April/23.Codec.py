'''
535. Encode and Decode TinyURL
Medium

1292

2493

Add to List

Share
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:

Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
 

Example 1:

Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"

Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after deconding it.
 

Constraints:

1 <= url.length <= 104
url is guranteed to be a valid URL.
Accepted
176,706
Submissions
210,088
'''
using one dictionary
class Codec:
    
    def __init__(self):
        self.d = {}
        self.count = 0
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.d[str(self.count)] = longUrl
        self.count += 1
        return str(self.count - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]
        

#using list
class Codec:
    
    def __init__(self):
        self.urls = []
        
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls.append(longUrl)
        return 'http://tinyurl.com/'+str(len(self.urls)-1)
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl.split('/')[-1])]
        
class Codec:
    
    alphabets = string.ascii_letters + '0123456789'
    
    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabets) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/'+ self.url2code[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))