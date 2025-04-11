import requests
import json


url = 'https://bonserver.onrender.com/entries'

#accesses all foods in sql database, returns as json
def get_food():
   try:
        response = requests.get(url)
        response.raise_for_status()  
      
        return response.json()
   except requests.exceptions.RequestException as error:
        print('Error:', error)
        
out = get_food() #output json
with open("ooss.json", "w") as json_file:
    json.dump(out, json_file, indent=4)
    
foods = []
for i in out: #iterates through json and appends to list
    foods.append(list(i.values()))

#test print each item
for i in foods:
    print(i)
    print("\n")

print(len(foods))