from icecream import ic

from enum import Enum
from data.load_data import load_cars_from_json
from data.save_data import save_cars_to_json
from helpers.functionality import print_cars_info, add_car, del_car, upd_car
from helpers.clear_terminal import clear_screen

class Actions(Enum):
    INFO = 1
    ADD = 2
    DELETE = 3
    UPDATE = 4
    EXIT = 5

def menu():
    for action in Actions: print(f'{action.value} - {action.name}')
    return Actions(int(input('Select one: ')))

if __name__ == '__main__':
    clear_screen()
    cars_data = load_cars_from_json('data/cars_list.json')
    while True:
        user_selection = menu()
        if user_selection == Actions.EXIT: 
            save_cars_to_json(cars_data, 'data/cars_list.json')
            exit()
        if user_selection == Actions.INFO:
            clear_screen() 
            print_cars_info(cars_data)
        if user_selection == Actions.ADD:
            clear_screen() 
            add_car(cars_data)
            save_cars_to_json(cars_data, 'data/cars_list.json')
        if user_selection == Actions.DELETE: 
            clear_screen()
            del_car(cars_data)
            save_cars_to_json(cars_data, 'data/cars_list.json')
        if user_selection == Actions.UPDATE: 
            clear_screen()
            upd_car(cars_data)
            save_cars_to_json(cars_data, 'data/cars_list.json')