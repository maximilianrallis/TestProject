import requests as requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
response

response.json()


photos = response.json()["photos"]
print(f"Found {len(photos)} photos")

print(photos[5]["img_src"])