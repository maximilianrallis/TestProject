from googleapiclient.discovery import build

api_key = 'AIzaSyD89wd3RXw0QRrUmyvRR_XeGcCZcD0B74g'

youtube = build("youtube", "v3", developerKey= api_key)

request = youtube.channels().list(
        part="statistics",
        forUsername="schafer5",
    )


response = request.execute()
