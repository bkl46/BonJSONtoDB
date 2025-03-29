import json
from sendp import add_entry
import re

file_name = "fribley_02_21_2025.json"

# Global 2D list to store extracted data
data_store = []

def extract_tag(item, key, label=None):
    """Extracts and returns a key's value from JSON, supports nested structures."""
    try:
        value = item.get(key, "n/a")
        if isinstance(value, dict):  # Handle cases like ordered_cor_icon
            extracted = [icon["label"] for icon in value.values()]
            result = ", ".join(extracted)
        elif isinstance(value, str):
            result = value
        else:
            result = "n/a"
        return result
    except Exception as e:
        print(f"Error extracting {key}: {e}")
        return "n/a"

def extract_nutrition_details(item, key):
    """Extracts nested nutrition details."""

    try:
        details = item.get(key, {})
        extracted_details = []
        for _, value in details.items():
            label = value.get("label", "n/a")
            val = value.get("value", "n/a")
            unit = value.get("unit", "")
            val = re.sub(r'\D', '', val)
           
            extracted_details.append(f"{val}")
        return extracted_details
    except Exception as e:
        print(f"Error extracting {key}: {e}")
        return ["n/a"]

def search(item):
    """Searches for key attributes in JSON and stores results in a 2D list."""
    if "label" in item:
        food_item = [item["label"]]  # Start with the label

        # Extract individual attributes
        food_item.append(extract_tag(item, "ordered_cor_icon"))
        food_item.append(extract_tag(item, "nutrition"))
        food_item.append(extract_tag(item, "station"))

        # Extract nutrition details (flattening lists)
        food_item.extend(extract_nutrition_details(item, "nutrition_details"))
        food_item.extend(extract_nutrition_details(item, "side_nutrition_details"))

        data_store.append(food_item)  # Store in 2D array

        # Search nested options
        if "options" in item and isinstance(item["options"], dict):
            search_nested_values(item["options"])
    else:
        print("Label does not exist, ignoring.")

def search_nested_values(item):
    """Recursively searches nested 'values' arrays."""
    if "values" in item and isinstance(item["values"], list):
        for value_item in item["values"]:
            search(value_item)

# Open and read the JSON file
with open(file_name, "r") as file:
    data = json.load(file)

# Loop through dictionary values
for item in data.values():
    search(item)

# Print or process the stored data
"""
for food in data_store:
    print(food)
 
    """
    

for i in range(1, len(data_store)):
    print("trial: ", i)
    add_entry(data_store[i])  


    
l =   """
    {'c1': 'Cornflakes', 'c2': '110', 'c3': '1.0', 'c4': '0', 'c5': '0', 'c6': '0', 'c7': '0', 'c8': '230', 'c9': '27', 'c10': '1', 'c11': '3', 'c12': '2', 'c13': False, 'c14': True, 'c15': False, 'c16': False, 'c17': False, 'c18': False, 'c19': False, 'c20': False}
    {'c1': 'Corn Chex', 'c2': '110', 'c3': '1.0', 'c4': '0.5', 'c5': '0', 'c6': '0', 'c7': '0', 'c8': '210', 'c9': '25', 'c10': '1', 'c11': '3', 'c12': '2', 'c13': False, 'c14': True, 'c15': True, 'c16': False, 'c17': False, 'c18': False, 'c19': False, 'c20': False}
    """
