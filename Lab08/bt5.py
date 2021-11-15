import urllib.request
req = urllib.request.Request('http://www.python.org/fish.html')
try :
    urllib.request.urlopen(req)
except urllib.request.HTTPError as e:
    print(e.code)
