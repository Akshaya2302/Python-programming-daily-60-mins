import requests

def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Check if the connection worked
        
        data = response.json()
        
        timestamp = data['timestamp']
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        
        print("\n--- ISS CURRENT LOCATION ---")
        print(f"Timestamp: {timestamp}")
        print(f"Latitude:  {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Check it on Google Maps: https://www.google.com/maps?q={latitude},{longitude}")

    except Exception as e:
        print(f"Could not fetch data: {e}")

if __name__ == "__main__":
    get_iss_location()
