import urllib.request
 
url_google = urllib.request.urlopen('https://www.google.com/')
print(url_google.read())
