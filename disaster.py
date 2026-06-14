import requests
import sys

main_url = 'https://api.terraquakeapi.com/v1/earthquakes/today'

def earthquake():
  response = requests.get(main_url, params={'limit': 10})
  data = response.json()
  print(f"Total earthquakes today: {data['totalEarthquakes']}")

  quake_limit = int(sys.argv[2])

  for quake in data['payload']:
      props = quake['properties']

      print(f"Time: {props['time']}")
      print(f"Magnitue: {props['mag']}")
      print(f"Location: {props['place']}")

earthquake()