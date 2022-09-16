from bs4 import BeautifulSoup
import requests

# Created by Colin Noel 
# This program web scrapes pricecharting.com for 2nd hand pricing of a used video game

class Game:

    def __init__(self, title, console, condition):
        self.title = title
        self.console = console
        self.condition = condition
        
        
    
    def show(self):
        print(F"{self.condition} {self.title} on {self.console} is:")

    def getGamePrice(self): # Returns a String for the price of a game
        
        # Console ID Dictionary for URL pathing as set by pricecharting.com
        consoleDict = {"nintendo ds":"G5","nintendo 3ds":"G39","nintendo switch":"G59",
                      "xbox 360":"G10","playstation 4":"G53","playstation 3":"G12"
                     ,"playstation 2":"G7","playstation 1":"G6","nintendo wii":"G11",
                      "nintendo wii U":"G47","gameboy advance":"G1","nintendo 64":"G4"}
        consoleID = consoleDict[self.console.lower()]
        
        # --- Pricecharting.com URL Parameters ---

        # Game Name: 'q=pokemon+diamond'
        # Game Region: '&region-name=ntsc'
        # Game Console: '&console-uid='
        # Exclude Variants?: '&exclude-variants=true'
        # Price Query or Marketplace: '&type=prices'
        # Sort By: '&sort=name'

        # 1) Use a base URL to give us the best chance of finding our desired game at the top of the results
        # 2) Customize the URL with our game name and console ID variables
        
        baseURL = "https://www.pricecharting.com/search-products?q="
        title_query = self.title.lower().replace(" ", "+")
        console_query = "&console-uid=" + consoleID
        default_filters = "&type=prices&sort=popularity&broad-category=video-games&console-uid=&region-name=ntsc&exclude-variants=false"
        url = baseURL + title_query + console_query + default_filters
        
        # Send HTTP get request to our customized URL
        webPage = requests.get(url)
        soup = BeautifulSoup(webPage.content, "html.parser")

        results = soup.find("tbody")
        firstRow = results.find("tr")

        cibPrice = firstRow.find("td",class_="price numeric cib_price")
        loosePrice = firstRow.find("td",class_="price numeric used_price")
        newPrice = firstRow.find("td",class_="price numeric new_price")

        # Searching Pricecharting.com for a game has two possible outcomes:
            # (1) Table of search results with different versions and game prices, by condition
            # (2) Product page of a specific game and version with prices, by condition

        # Under outcome (1), we find cibPrice from the element
        if cibPrice != None: 
    
            if self.condition == "cib": return float(cibPrice.get_text().strip()[1:])
            elif self.condition == "loose": return float(loosePrice.get_text().strip()[1:])
            elif self.condition == "new": return float(newPrice.get_text().strip()[1:])
            else: print("Please input a correctly syntaxed game condition")
        
        # Under outcome (2) below, cibPrice will return None, since the product page has a 
        # different element for a game's cib price
        
        else:
            ProdPgLooseID = firstRow.find("td",id="used_price")
            ProdPgLoosePrice = ProdPgLooseID.find("span",class_="price js-price")
            
            ProdPgCibID = firstRow.find("td",id="complete_price")
            ProdPgCibPrice = ProdPgCibID.find("span",class_="price js-price")
            
            ProdPgNewID = firstRow.find("td",id="new_price")    
            ProdPgNewPrice = ProdPgNewID.find("span",class_="price js-price")

            if self.condition == "cib": return float(ProdPgCibPrice.get_text().strip()[1:])
            elif self.condition == "loose": return float(ProdPgLoosePrice.get_text().strip()[1:])
            elif self.condition == "new": return float(ProdPgNewPrice.get_text().strip()[1:])
            else: print("Please input a correctly syntaxed game condition")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# g = Game("Pokemon Platinum","nintendo DS","cib")
# g.show()
# print(g.getGamePrice())
