import requests
import json
import re

# Define the URL
url = 'https://bonserver.onrender.com/entries'

def get_food():
   try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
      
        return response.json()
   except requests.exceptions.RequestException as error:
        print('Error:', error)
        
out = get_food()
with open("oo.json", "w") as json_file:
    json.dump(out, json_file, indent=4)
    
foods = []
for i in out:
    foods.append(list(i.values()))

for i in foods:
    print(i)
    print("\n")

