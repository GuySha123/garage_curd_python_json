from icecream import ic

def print_cars_info(cars_data):
    cars = cars_data.get("cars", [])

    if not cars:
        ic("Amount of cars in the garage: 0")
        return

    ic(f"Amount of cars in the garage: {len(cars)}")
    for index, car in enumerate(cars, start=1):
        ic(f"({index}) Type: {car["car_type"]}, Color: {car["color"]}, Model: {car["model"]}")

def add_car(cars_data):
    cars = cars_data.get("cars", [])
    new_car = {"car_type": input("Car type? "), "color": input("Car color? "), "model": int(input("Car model (year only)? "))}
    cars.append(new_car)
    ic(f"New car added: Type: {new_car['car_type']}, Color: {new_car['color']}, Model: {new_car['model']}")

def find_car(cars_data):
    print_cars_info(cars_data)
    car_search = int(input("Select car's number from the list: "))
    return car_search - 1

def del_car(cars_data):
    car_index = find_car(cars_data)
    if 0 <= car_index < len(cars_data.get("cars", [])):
        removed_car = cars_data["cars"].pop(car_index)
        ic(f"Deleted car - Type: {removed_car["car_type"]}, Color: {removed_car["color"]}, Model: {removed_car["model"]}")
    else:
        ic("Invalid selection")


def upd_car(cars_data):
    car_index = find_car(cars_data)
    cars = cars_data.get("cars", [])
    
    if 0 <= car_index < len(cars):
        old_car = cars[car_index]
        cars[car_index] = {"car_type": input("Car type? "), "color": input("Car color? "), "model": int(input("Car model (year only)? "))}
        new_car = cars[car_index]
        
        ic(f"Updated car from - Type: {old_car['car_type']}, Color: {old_car['color']}, Model: {old_car['model']}")
        ic(f"Updated car to - Type: {new_car['car_type']}, Color: {new_car['color']}, Model: {new_car['model']}")
    else:
        ic("Invalid selection")
    cars_data["cars"] = cars