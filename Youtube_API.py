from googleapiclient.discovery import build

api_key = 'AIzaSyD89wd3RXw0QRrUmyvRR_XeGcCZcD0B74g'

youtube = build("youtube", "v3", api_key)

search_response = youtube.search().list(

                                        ).execute()

request = youtube.channels().list(part= "statistics",forUsername= "schafer5")

response = request.execute()

print(response)