import requests
import json, csv
import pandas as pd

API_KEY = 'AIzaSyALrKc3-W0u_Ku-J2OpyjnqFhV5wKlwKGs'
list_video_id = ['7cmvABXyUC0', '9eH-7x7swEM', 'JndzGxbwvG0', 'l0P5_E6J_g0']
fieldnames = ['videoid', 'viewCount', 'likeCount', 'dislikeCount', 'favoriteCount', 'commentCount']
rows = []
for video_id in list_video_id:
    url = "https://www.googleapis.com/youtube/v3/videos?id=" + video_id + "&part=statistics&key=" + API_KEY
    response = requests.get(url).json()
    for i in response['items']:
        rows.append({"videoid": i['id'],
                     "viewCount": i['statistics']['viewCount'],
                     "likeCount": i['statistics']['likeCount'],
                     "dislikeCount": i['statistics']['dislikeCount'],
                     "favoriteCount": i['statistics']['favoriteCount'],
                     "commentCount": i['statistics']['commentCount']})
print(rows)
with open(r'get_api_youtube.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for j in rows:
        writer.writerow(j)
