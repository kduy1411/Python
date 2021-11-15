import requests
from bs4 import BeautifulSoup

url = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages'
response = requests.get(url)
suop = BeautifulSoup(response.text, 'html.parser')
images = suop.find_all('img')


for index, image in enumerate(images):
    image_url= ('https://developer.mozilla.org'+image.get("src"))    
    
    image_extension= image_url.split(".")[-1]  
    image_bytes = requests.get(image_url).content
    
    if image_bytes:
        with open(f"Image {index+1}.{image_extension}", "wb") as file:
            file.write(image_bytes)
            print(f"Downloading image {index+1}.{image_extension}")
