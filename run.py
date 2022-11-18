"""
Import Libraries:
gspread to deal with google sheet api
google.oauth2 for Credentials
"""
import os
import sys
from time import sleep
import gspread
import inquirer
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPE_CREDS = CREDS.with_scopes(SCOPE)
GSPEAD_CLIENT = gspread.authorize(SCOPE_CREDS)
SHEET = GSPEAD_CLIENT.open("shahem_inventory")

def show_list():
    """


    """
    print("Welcome to Shahem inventory Data Automation \n")
    questions = [
        inquirer.List("choice",
        message="What would like to do?",
        choices=["Add sales", "Add buy", "Add damage", "Return to stock",
        "Return to damage", "Empty space for storage", "Exit"],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers == {'choice': 'Add sales'}:
        main_sales()
    elif answers == {'choice': 'Add buy'}:
        main_buy()
    elif answers == {'choice': 'Add damage'}:
        main_damage()
    elif answers == {'choice': 'Return to stock'}:
        main_return_stock()
    elif answers == {'choice': 'Return to damage'}:
        main_return_damage()
    elif answers == {'choice': 'Empty space for storage'}:
        empty_space_for_storage()
    else:
        print("thank you")
        sys.exit()


def main():
    """

    """
    os.system("clear")
    show_list()


def go_back():
    """

    """
    questions = [
        inquirer.List("choice",
        message="What would like to do?",
        choices=["Go back", "Exit"],
        ),
    ]
    answers = inquirer.prompt(questions)
    if answers == {'choice': 'Go back'}:
        main()
    else:
        print("thank you")
        sys.exit()


def main_sales():
    """
    central method for sales
    """
    sales_data = get_input('sales')
    sales = [int(num) for num in sales_data]
    update_worksheet(sales, 'sales')
    update_stock_worksheet_deduct(sales)
    sleep(2)
    go_back()
    


def main_buy():
    '''
     central method for buy
    '''
    bay_data = get_input('buy')
    buy = [int(num) for num in bay_data]
    update_worksheet(buy, 'buy')
    update_stock_worksheet_add(buy)
    sleep(2)
    go_back()


def main_damage():
    """
    central method for damage
    """
    damage_data = get_input('damage')
    damage = [int(num) for num in damage_data]
    update_damage_worksheet_add(damage)
    update_stock_worksheet_deduct(damage)
    sleep(2)
    go_back()


def main_return_stock():
    """
    central method for return to stock
    """
    return_stock_data = get_input('return to stock')
    return_stock = [int(num) for num in return_stock_data]
    update_stock_worksheet_add(return_stock)
    sleep(2)
    go_back()


def main_return_damage():
    """
    central method for return to damage
    """
    return_damage_data = get_input('return to damage')
    return_damage = [int(num) for num in return_damage_data]
    update_damage_worksheet_add(return_damage)
    sleep(2)
    go_back()



def empty_space_for_storage():
    """
    s
    """
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    row = []
    for num in stock_row:
        new_num = num.replace(',', '')
        row.append(new_num)
    int_row = [int(num) for num in row]
    storage = []
    for num in int_row:
        if num < 1000:
            empty_storage = 1000 - num
            storage.append(empty_storage)
        else:
            storage.append("storage is full")
    print("T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL")
    print(f"Empty space for storage :{storage}")
    sleep(2)
    go_back()



def get_input(sheet_type):
    """
    Get sheet figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print(f"Please enter {sheet_type} data from the last market.")
        print("T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:\n")
        new_data = data_str.split(",")

        if validate_data(new_data):
            print("data is valid")
            break
    return new_data


def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        values = [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(data, sheet_type):
    """
    Update worksheet, add new row with the list data provided
    and print total in worksheet
    """
    print(f"Updating {sheet_type} worksheet...\n")
    worksheet = SHEET.worksheet(sheet_type)
    worksheet.append_row(data)
    print(f"{sheet_type} worksheet updated successfully.\n")
    calculate_total(sheet_type)


def calculate_total(data):
    """
    Calculate total for each sheet
    """
    total = []
    for i in range(1, 7):
        col = SHEET.worksheet(data).col_values(i)
        col.pop(0)
        new_col = [int(num.replace(',', '')) for num in col]
        total_sum = sum(new_col)
        total.append(total_sum)
    print("Products: T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL")
    print(f"Total {data}: {total} .\n")


def update_stock_worksheet_deduct(data):
    """
    Update stock worksheet, add new row with
    the list data provided - the old stock
    """
    print("Updating stock worksheet...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    new_stock = []
    for stock, num in zip(stock_row, data):
        stock_data = int(stock.replace(',', '')) - num
        new_stock.append(stock_data)
    SHEET.worksheet("stock").append_row(new_stock)
    print("stock worksheet updated successfully.\n")
    print("Products: T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL")
    print(f"The new stock: {new_stock} .\n")


def update_stock_worksheet_add(data):
    """
    Update stock worksheet, add new row with
    the list data provided + the old stock
    """
    print("Updating stock worksheet...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    new_stock = []
    for stock, num in zip(stock_row, data):
        stock_data = int(stock.replace(',', '')) + num
        new_stock.append(stock_data)
    SHEET.worksheet("stock").append_row(new_stock)
    print("stock worksheet updated successfully.\n")
    print("Products: T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL")
    print(f"The new stock: {new_stock} .\n")


def update_damage_worksheet_add(data):
    """
    Update damage worksheet, add new row with
    the list data provided + the old damage
    """
    print("Updating damage worksheet...\n")
    damage = SHEET.worksheet("damage").get_all_values()
    damage_row = damage[-1]
    new_damage = []
    for damage, num in zip(damage_row, data):
        damage_data = int(damage.replace(',', '')) + num
        new_damage.append(damage_data)
    SHEET.worksheet("damage").append_row(new_damage)
    print("damage worksheet updated successfully.\n")
    print("Products: T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL")
    print(f"The new total damage: {new_damage} .\n")


main()
