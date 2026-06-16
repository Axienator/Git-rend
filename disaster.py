import requests
from argparse import ArgumentParser

main_url = 'https://api.terraquakeapi.com/v1/earthquakes/recent'

def earthquake() -> None:
  parser = ArgumentParser(description='fetches information about the TerraQuake API')
  parser.add_argument('--limit', default=10)
  args = parser.parse_args()

  response = requests.get(main_url, params={'limit':args.limit})

  if response.status_code == 200:
    data = response.json()
    for item in data['payload']:

      result = item['properties']

      print(f"Magnitude: {result['mag']}")
      print(f"Time: {result['time']}")
      print("-" * 20)
  else:
    print(f"Error:{response.status_code}")

if __name__ == "__main__":
  earthquake()