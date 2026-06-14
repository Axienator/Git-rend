import requests

response = requests.get(
  'https://api.terraquakeapi.com/v1/earthquakes/today',
  params={'limit': 10}
)
data = response.json()
print(f"Total earthquakes today: {data['totalEarthquakes']}")

for quake in data['payload']:
    props = quake['properties']

    print(f"Time: {props['time']}")
