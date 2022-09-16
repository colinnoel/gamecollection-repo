# author: Colin Noel

from bs4 import BeautifulSoup
import requests
import csv

game_name = input('Enter game name: ')
console_name = input('Enter console: ')
game_condition = input('Enter condition (loose, cib, or new): ')
print()

# Console ID Dictionary for URL pathing as set by pricecharting.com
consoleIDs = {"nintendo ds":"G5","nintendo 3ds":"G39","nintendo switch":"G59",
              "xbox 360":"G10","playstation 4":"G53","playstation 3":"G12"
              ,"playstation 2":"G7","playstation 1":"G6","nintendo wii":"G11",
              "nintendo wii U":"G47","gameboy advance":"G1"}

cID = consoleIDs[console_name.lower()]
g = game_name.replace(" ", "+")

# --- Pricecharting.com URL Parameter: Example ---

# Game Name: 'q=pokemon+diamond'
# Game Region: '&region-name=ntsc'
# Game Console: '&console-uid='
# Exclude Variants?: '&exclude-variants=true'
# Price Query or Marketplace: '&type=prices'
# Sort By: '&sort=name'
# ---                                  ---

# Use a base URL to give us the best chance of finding our desired game at the top of the results
# Customize the URL with our game name and console ID varialbes

URL = "https://www.pricecharting.com/search-products?q=" + g.lower() + "&console-uid=" + cID + "&type=prices&sort=popularity&broad-category=video-games&console-uid=&region-name=ntsc&exclude-variants=false"

# Send HTTP get request to our customized URL
webPage = requests.get(URL)
soup = BeautifulSoup(webPage.content, "html.parser")


# Searching Pricecharting.com for a game has two possible outcomes:
    # (1) Table of search results with different versions and game prices, by condition
    # (2) Product page of a specific game and version with prices, by condition

results = soup.find("tbody")
firstRow = results.find("tr")

cibPrice = firstRow.find("td",class_="price numeric cib_price")
loosePrice = firstRow.find("td",class_="price numeric used_price")
newPrice = firstRow.find("td",class_="price numeric new_price")


# Under outcome (1) we find cibPrice from the element
if cibPrice != None: 
    
    if game_condition == "cib":
        print(F"Current CIB Price: {cibPrice.get_text()}")
        
    elif game_condition == "loose":
        print(F"Current Loose Price: {loosePrice.get_text()}") 
        
    else:
        print(F"Current New Price: {newPrice.get_text()}") 
    
    
# Under outcome (2) cibPrice will return None, since the product page has a different element for a game's cib price
else:
    
    ProdPgLooseID = firstRow.find("td",id="used_price")
    ProdPgLoosePrice = ProdPgLooseID.find("span",class_="price js-price")
    
    ProdPgCibID = firstRow.find("td",id="complete_price")
    ProdPgCibPrice = ProdPgCibID.find("span",class_="price js-price")
    
    ProdPgNewID = firstRow.find("td",id="new_price")    
    ProdPgNewPrice = ProdPgNewID.find("span",class_="price js-price")
    

    if game_condition == "cib":
        print(F"Current CIB Price: {ProdPgCibPrice.get_text().strip()}")
        
    elif game_condition == "loose":
        print(F"Current Loose Price: {ProdPgLoosePrice.get_text().strip()}")
        
    else:
        print(F"Current New Price: {ProdPgNewPrice.get_text()}") 




print()  
print("Your URL is: " + URL)