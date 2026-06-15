import requests
from argparse import ArgumentParser

main_url = 'https://api.terraquakeapi.com/v1/earthquakes'

def earthquake() -> None:
  parser = ArgumentParser(description='fetches information about the TerraQuake API')
  parser.add_argument('--limit')
  args = parser.parse_args()

  response = requests.get(main_url, params={'limit':args})

  if response.status_code == 200:
    data = response.json()
    print(f"Total earthquakes today: {data['totalEarthquakes']}")
  else:
     print(f"Error:{response.status_code}")

earthquake()