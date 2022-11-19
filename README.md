# Shahem inventory
- Shahem inventory is a site that hopes to demonstrate how pure python works in a real-world context. 
- The site will be targeted users who want to get report over there inventory after the inter data.
- It will show that the storage is full if the stock for ech item arrive to 1000
- Shahem inventory is a application will have a command line interface in python.
- Shahem inventory site will show the users the a lest of options:
  - Add sales.
  - Add buy.
  - Add damage.
  - Return to stock.
  - Return to damage.
  - Storage capacity.
  - Exit.

[Shahem inventory](https://shahem-inventory.herokuapp.com/) site.


![Responsive Mockup]()

# Navigator

- [**User experience UX**](<#user-experience-ux>)
    - [User stories](<#user-stories>)
    - [Flow chart diagram](<#flow-chart-diagram>)
    - [Site structure](<#site-structure>)
    - [Data Model](<#data-model>)



# User experience (UX)

## User stories

- As a user, I want to understand the purpose of this site upon loading it.
- As a user, I want to be able to know what are the instructions to use this site.
- As a user, I want to be able to add sales to the total sales and update the stock.
- As a user, I want to be able to add buy to the total buy and update the stock.
- As a user, I want to be able to add damage to the total damage and update the stock.
- As a user, I want to be able to return to stock update the stock.
- As a user, I want to be able to return to damage update the damage.
- As a user, I want to be able to see storage capacity.
- As a user, I want to be able to exit site.
- As a user I want have an easy way of getting back to the main menu.


[Back to top](<#navigator>)

## Flow chart diagram

- The site steps overview.
- Explain the flow of the site.
- Shows the sequence of triggering the site's functionalities.
- Plan and write efficient functions.


![flow-chart-diagram ]()


[Back to top](<#navigator>)

## Site structure

- Shahem inventory is a terminal based application that is being presented in a one page website.
- When the application starts the user see a short welcome message, the instructions and a list of choices
 
[Back to top](<#navigator>)

## Data Model

To store all data in the application I made a choice to use Google Sheets. All data in the application is being sent and retrieved from the Google Sheet.

- Name of workbook: shahem_inventory
- Name of worksheet: sales
- Name of worksheet: buy
- Name of worksheet: damage
- Name of worksheet: stock

The worksheet holds 6 columns with information such as:
  T-shirt XS,T-shirt S,T-shirt M,T-shirt L,T-shirt XL,T-shirt XXL 
  that is being controlled from the application via Python.

![data-model]()
![data-model]()
![data-model]()
![data-model]()
 
[Back to top](<#navigator>)

