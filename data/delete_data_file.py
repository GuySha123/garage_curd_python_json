import os

def del_cars_file(filename):
    try:
        os.remove(filename)
        print(f'Cars data file has been deleted.')
    except FileNotFoundError:
        print(f'{filename} not found.')
    except Exception as e:
        print(f"Error deleting file: {e}")