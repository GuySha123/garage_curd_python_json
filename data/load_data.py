import json

def load_cars_from_json(filename):
    global cars
    try:
        with open(filename, 'r') as f:
            cars = json.load(f)
    except:
        print('File not found')
        cars = {"cars": []}
    return cars