# Garage with json files using Python

A simple program to practice CRUD with json files

## Functions

`data/load_data.py`

-   **load_cars_from_json**: Loads car data from a JSON file. Initializes with an empty list if the file doesn't exist or is invalid.
-   **save_cars_to_json**: Saves car data to a JSON file.
-   **delete_cars_file**: Deletes the car data file if it exists.

`helpers/functionality.py`

-   **print_cars_info**: Prints information of all cars.
-   **add_car**: Adds a new car to the list with user input for car type, color, and model year.
-   **find_car**: Displays cars and prompts user to select one by number.
-   **del_car**: Deletes a car from the list based on user selection.
-   **upd_car**: Updates car information based on user selection.

`helpers/clear_terminal.py`

**clear_screen**: Clears the console screen.

`main.py`

-   **menu**: Displays action menu and prompts user to select one.
-   **Main Script Execution**: Loads car data, displays menu, performs actions (display, add, delete, update, delete file), and saves updates.

## Get started

1. Ensure Python is installed.
2. Clone the repository:
    ```
    git clone https://github.com/GuyShalevWP/garage_curd_python_json.git
    ```
3. Add virtual environment (env):

    ```
    py -m virtualenv env
    ```

    `or`

    ```
    python -m virtualenv env
    ```

4. Active env:
    ```
    .\env\Scripts\activate
    ```
5. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```
6. Run `app.py` to start the application:

    ```
    py ./app.py
    ```

    `or`

    ```
    python ./app.py
    ```
