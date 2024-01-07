import requests

def get_active_listings(api_key, offset=0, limit=100):
    """Fetch a list of active listings from the Etsy API."""
    url = 'https://openapi.etsy.com/v3/application/listings/active'
    headers = {
        'x-api-key': api_key,
    }
    params={
        'limit': limit,
        'offset': offset
    }

    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        try:
         print(response.status_code)
         error_message = response.json().get('error')
         print(f"Error retrieving listings: {error_message}")
        except ValueError:
            print("Error retrieving listings: %s" % response.text)
        return None
    else:
        return response.json()  # Add this line to return the response data


