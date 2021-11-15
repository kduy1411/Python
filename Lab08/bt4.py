import urllib.request
try:
    url_google = urllib.request.urlopen('https://www.huynhhoc.com')
    print(url_google.read())
except urllib.error.URLError as e:
    print("Error: ", e.reason)
