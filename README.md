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


![Responsive Mockup](./assets/images/amiresponsive.PNG)

# Navigator

- [**User experience UX**](<#user-experience-ux>)
    - [User stories](<#user-stories>)
    - [Flow chart diagram](<#flow-chart-diagram>)
    - [Site structure](<#site-structure>)
    - [Data Model](<#data-model>)
- [**Features**](<#features>)
    - [Existing features](<#existing-features>)
    - [Python functions](<#python-functions>)
        - [Show list](<#show-list>)
        - [Main](<#main>)
        - [Go back](<#go-back>)
        - [Main sales](<#main-sales>)
        - [Main buy](<#main-buy>)
        - [Main damage](<#main-damage>)
        - [Main return stock](<#main-return-stock>)
        - [Main return damage](<#main-return-damage>)
        - [Storage capacity](<#storage-capacity>)
        - [Get input](<#get-input>)
        - [Validate data](<#validate-data>)
        - [Update worksheet](<#update-worksheet>)
        - [Calculate total](<#calculate-total>)
        - [Update stock worksheet deduct](<#update-stock-worksheet-deduct>)
        - [Update stock worksheet add](<#update-stock-worksheet-add>)
        - [Update damage worksheet add](<#update-damage-worksheet-add>)
    - [Future features](<#future-features>)


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

<details><summary><b>Flow chart diagram</b></summary>

![flow-chart-diagram ](./assets/images/Flow-chart-diagram.PNG)
</details><br/>

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

 <details><summary><b>Google Sheet sales</b></summary>

![Google Sheet](./assets/images/worksheet-sales.PNG)
</details><br/>
 <details><summary><b>Google Sheet buy</b></summary>

![Google Sheet](./assets/images/worksheet-buy.PNG)
</details><br/>
<details><summary><b>Google Sheet damage</b></summary>

![Google Sheet](./assets/images/worksheet-damage.PNG)
</details><br/>
 <details><summary><b>Google Sheet stock</b></summary>

![Google Sheet](./assets/images/worksheet-stock.PNG)
</details><br/>


[Back to top](<#navigator>)

# Features 

## Existing features

## Python functions

### Show list


<details><summary><b>Show list</b></summary>

![Show list](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Main


<details><summary><b>Main</b></summary>

![Main](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Go back


<details><summary><b>Go back</b></summary>

![Go back](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Main sales


<details><summary><b>Main sales</b></summary>

![Main sales](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Main buy


<details><summary><b>Main buy</b></summary>

![Main buy](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Main damage


<details><summary><b>Main damage</b></summary>

![Main damage](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Main return stock


<details><summary><b>Main return stock</b></summary>

![Main return stock](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Main return damage


<details><summary><b>Main return damage</b></summary>

![Main return damage](./assets/images/)
</details><br/>

[Back to top](<#navigator>)

### Storage capacity


<details><summary><b>Storage capacity</b></summary>

![Storage capacity](./assets/images/)
</details><br/>

[Back to top](<#navigator>)


### Get input

[Back to top](<#navigator>)


### Validate data

[Back to top](<#navigator>)


### Update worksheet

[Back to top](<#navigator>)


### Calculate total

[Back to top](<#navigator>)


### Update stock worksheet deduct

[Back to top](<#navigator>)


### Update stock worksheet add

[Back to top](<#navigator>)


### Update damage worksheet add

[Back to top](<#navigator>)




