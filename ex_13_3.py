import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'count': '2'})
print(url)

#ignore SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection1 = urllib.request.urlopen(url, context=ctx)
data = connection1.read()
print(data)
print("============================")
headers = dict(connection1.getheaders())
print(headers)
