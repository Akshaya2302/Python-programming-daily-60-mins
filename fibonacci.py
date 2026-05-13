import urllib.request
import json

def tell_me_a_joke():
    # This is a free, public API that returns a random joke in JSON format
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            
            # Convert the JSON web response into a Python dictionary
            joke = json.loads(data)
            
            print("Here's a joke from the internet for you:\n")
            
            # Extract the 'setup' part of the joke
            print(f"🤔 {joke['setup']}")
            
            # Use input() just to pause the script before revealing the answer
            input("(Press Enter for the punchline...)")
            
            # Extract the 'punchline'
            print(f"😂 {joke['punchline']}\n")
            
    except Exception as e:
        print("Oops! I couldn't fetch a joke. Are you connected to the internet?")
        print(f"Error details: {e}")

tell_me_a_joke()
