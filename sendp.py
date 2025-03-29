import requests
import json

# Define the URL
url = 'https://bonserver.onrender.com/entries'

# Define the request body
def add_entry(food):
    url = 'https://bonserver.onrender.com/entries'
    data = {}
    if(len(food) > 14):
        data = {
            "c1": food[0],
            "c2": food[4],
            "c3": food[5],
            "c4": food[6],
            "c5": food[7],
            "c6": food[8],
            "c7": food[9],
            "c8": food[10],
            "c9": food[11],
            "c10": food[12],
            "c11": food[13],
            "c12": food[14],
            "c13": "Vegetarian" in food[1],
            "c14": "Vegan" in food[1],
            "c15": "Made without Gluten-Containing Ingredients" in food[1],
            "c16": "In Balance" in food[1],
            "c17": "Halal" in food[1],
            "c18": "Farm to Fork" in food[1],
            "c19": "Humane" in food[1],
            "c20": "Often" in food[1],
            
        }
    print(data)
    # Define headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Make the POST request
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an error for bad status codes
        print(response.json())  # Print the response data
    except requests.exceptions.RequestException as error:
        print('Error:', error)
        
