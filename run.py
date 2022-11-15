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
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully.\n")


def update_stock_worksheet_add(data):
    """
    Update stock worksheet, add new row with
    the list data provided + the old stock
    """
    print("Updating stock worksheet...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    now_stock = []
    for stock, num in zip(stock_row, data):
        stock_data = int(stock) - num
        now_stock.append(stock_data)
    SHEET.worksheet("stock").append_row(now_stock)

    print("stock worksheet updated successfully.\n")


def main_sales():
    sales_data = get_input_sales()
    sales = [int(num) for num in sales_data]
    update_sales_worksheet(sales)
    update_stock_worksheet_add(sales)

print("Welcome to Shahem inventory Data Automation")


main_sales()
