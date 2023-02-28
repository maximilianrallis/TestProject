import os
os.environ['HTTP_PROXY'] = 'http://proxy.example.com:8080'
os.environ['HTTPS_PROXY'] = 'https://proxy.example.com:8080'

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from googleapiclient.discovery import build

api_key = 'AIzaSyD89wd3RXw0QRrUmyvRR_XeGcCZcD0B74g'

youtube = build("youtube", "v3", developerKey= api_key)

request = youtube.channels().list(
        part="statistics",
        forUsername="schafer5",
    )


response = request.execute()
