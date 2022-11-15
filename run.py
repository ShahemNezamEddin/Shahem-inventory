import gspread
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


def get_input_sales():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please inter sales data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Inter your data here: ")
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


def update_sales_worksheet(data):
    """
    Update sales worksheet, add new row with the list data provided
    and print total sales
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")
    total_sales = []
    for i in range(1,7):
        col = SHEET.worksheet("sales").col_values(i)
        col.pop(0)
        new_col = [int(num) for num in col]
        total = sum(new_col)
        total_sales.append(total)
        
    print(f"Total sales: {total_sales} .\n")


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
        stock_data = int(stock) - num
        new_stock.append(stock_data)
    SHEET.worksheet("stock").append_row(new_stock)
    print("stock worksheet updated successfully.\n")
    return new_stock


def main_sales():
    sales_data = get_input_sales()
    sales = [int(num) for num in sales_data]
    update_sales_worksheet(sales)
    new_stock_data = update_stock_worksheet_deduct(sales)


def get_input_buy():
    """
    Get buy figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please inter buy data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Inter your data here: ")
        new_data = data_str.split(",")

        if validate_data(new_data):
            print("data is valid")
            break
    return new_data

def update_buy_worksheet(data):
    """
    Update buy worksheet, add new row with the list data provided
    and print total buy
    """
    print("Updating buy worksheet...\n")
    sales_worksheet = SHEET.worksheet("buy")
    sales_worksheet.append_row(data)
    print("buy worksheet updated successfully.\n")
    total_buy = []
    for i in range(1,7):
        col = SHEET.worksheet("buy").col_values(i)
        col.pop(0)
        new_col = [int(num) for num in col]
        total = sum(new_col)
        total_buy.append(total)
        
    print(f"Total buy: {total_buy} .\n")
    
    
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
        stock_data = int(stock) + num
        new_stock.append(stock_data)
    SHEET.worksheet("stock").append_row(new_stock)
    print("stock worksheet updated successfully.\n")
    return new_stock
       


def main_buy():
    bay_data = get_input_buy()
    buy = [int(num) for num in bay_data]
    update_buy_worksheet(buy)
    new_stock_data = update_stock_worksheet_add(buy)



def get_input_damage():
    """
    Get damage figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please inter buy data from the last market.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Inter your data here: ")
        new_data = data_str.split(",")

        if validate_data(new_data):
            print("data is valid")
            break
    return new_data

def main_damage():
    damage_data = get_input_damage()



def main():
    main_sales()
    main_buy()
    main_damage()

print("Welcome to Shahem inventory Data Automation")

main()

