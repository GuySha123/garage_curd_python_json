import json

def save_cars_to_json(cars_data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(cars_data, f, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")
