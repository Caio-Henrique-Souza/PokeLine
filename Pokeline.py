import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://pokeapi.co/api/v2/pokemon/'
r = requests.get(url)
data = r.json()

print(data)