import requests

url = "https://zoopla-uk.p.rapidapi.com/properties/search-sale"
querystring = {
    "query": "South Kensington"
}

headers = {
    "x-rapidapi-host": "zoopla-uk.p.rapidapi.com",
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY" # Replace with your actual RapidAPI key
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
print(data['data']['listings']['regular'][0].keys())
print(data['data']['listings']['regular'][0]['address'])
