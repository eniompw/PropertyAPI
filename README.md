# Property Search Tool

A Python script for searching properties for sale in the UK using the Zoopla UK API via RapidAPI.

## Description

This project provides a simple interface to search for properties listed for sale on Zoopla, one of the UK's leading property portals. The script queries the Zoopla UK API and retrieves property listings based on location criteria.

## Features

- Search properties by location (area, postcode, or address)
- Retrieve property listing details
- Display available property information fields
- View property addresses

## Prerequisites

- Python 3.x
- `requests` library
- RapidAPI account with access to Zoopla UK API

## Installation

1. Clone this repository:
```bash
git clone https://github.com/eniompw/Property.git
cd Property
```

2. Install required dependencies:
```bash
pip install requests
```

3. Get your RapidAPI key:
   - Sign up at [RapidAPI](https://rapidapi.com/)
   - Subscribe to the [Zoopla UK API](https://rapidapi.com/vibapidev/api/zoopla-uk)
   - Copy your API key

4. Update the script with your API key:
   - Open `search.py`
   - Replace `YOUR_RAPIDAPI_KEY` with your actual RapidAPI key

## Usage

Run the script from the command line:

```bash
python search.py
```

The script will:
1. Search for properties in South Kensington (default location)
2. Print all available data fields for the first property
3. Display the address of the first property

### Customizing the Search

To search for properties in a different location, modify the `querystring` in `search.py`:

```python
querystring = {
    "query": "Your Location Here"  # e.g., "London", "SW7 2AZ", etc.
}
```

## Example Output

```
dict_keys(['listing_id', 'title', 'price', 'address', 'bedrooms', ...])
{'display_address': '123 Example Street, South Kensington, London SW7'}
```

## API Information

This project uses the Zoopla UK API provided through RapidAPI. The API provides comprehensive property data including:
- Property listings
- Prices
- Addresses
- Number of bedrooms/bathrooms
- Property descriptions
- Images
- And more

**API Reference:** [Zoopla UK API on RapidAPI](https://rapidapi.com/vibapidev/api/zoopla-uk)

## Project Structure

```
Property/
├── search.py       # Main search script
├── README.md       # This file
└── LICENSE         # License information
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms specified in the LICENSE file.

## Disclaimer

This tool is for educational and personal use. Please ensure you comply with Zoopla's Terms of Service and RapidAPI's usage policies when using this script.

## Support

For issues, questions, or contributions, please open an issue on the GitHub repository.