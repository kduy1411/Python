import urllib.request

url_google = urllib.request.urlopen('https://www.python.org/search/?q=urlopen&submit=Search')
print(url_google.read())
