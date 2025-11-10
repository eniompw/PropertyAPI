"""
Property Search Script
This script searches for properties for sale in the UK using the Zoopla UK API via RapidAPI.
"""

import requests

# API endpoint for searching properties for sale on Zoopla UK
url = "https://zoopla-uk.p.rapidapi.com/properties/search-sale"

# Query parameters - specify the location to search for properties
querystring = {
    "query": "South Kensington"  # Location to search (can be area, postcode, or address)
}

# Request headers containing API authentication credentials
headers = {
    "x-rapidapi-host": "zoopla-uk.p.rapidapi.com",  # API host
    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY"  # Replace with your actual RapidAPI key
}

# Make GET request to the API with headers and query parameters
response = requests.get(url, headers=headers, params=querystring)

# Parse the JSON response into a Python dictionary
data = response.json()

# Print all available keys/fields for the first property listing
print(data['data']['listings']['regular'][0].keys())

# Print the address of the first property in the search results
print(data['data']['listings']['regular'][0]['address'])
