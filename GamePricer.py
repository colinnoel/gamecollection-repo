from bs4 import BeautifulSoup
import requests

class Game:

    def __init__(self, title, console, condition, game_price_url,):
        self.title = title
        self.console = console
        self.condition = condition
        self.game_price_url = game_price_url
        
    
    def show(self):
        print(F"{self.condition} {self.title} on {self.console} is:")

    def getGamePrice(self): # Returns a String for the price of a game
        consoleDict = {"nintendo ds":"G5","nintendo 3ds":"G39","nintendo switch":"G59",
                      "xbox 360":"G10","playstation 4":"G53","playstation 3":"G12"
                     ,"playstation 2":"G7","playstation 1":"G6","nintendo wii":"G11",
                      "nintendo wii U":"G47","gameboy advance":"G1","nintendo 64":"G4"}
        consoleID = consoleDict[self.console.lower()]
        
        
        baseURL = "https://www.pricecharting.com/search-products?q="
        title_query = self.title.lower().replace(" ", "+")
        console_query = "&console-uid=" + consoleID
        default_filters = "&type=prices&sort=popularity&broad-category=video-games&console-uid=&region-name=ntsc&exclude-variants=false"
        url = baseURL + title_query + console_query + default_filters

        webPage = requests.get(url)
        soup = BeautifulSoup(webPage.content, "html.parser")

        results = soup.find("tbody")
        firstRow = results.find("tr")

        cibPrice = firstRow.find("td",class_="price numeric cib_price")
        loosePrice = firstRow.find("td",class_="price numeric used_price")
        newPrice = firstRow.find("td",class_="price numeric new_price")

        if cibPrice != None: 
    
            if self.condition == "cib": return [cibPrice.get_text().strip(),url]
            elif self.condition == "loose": return [loosePrice.get_text().strip(),url]
            elif self.condition == "new": return [newPrice.get_text().strip(),url]
            else: print("Please input a correctly syntaxed game condition")
        
        else:
            ProdPgLooseID = firstRow.find("td",id="used_price")
            ProdPgLoosePrice = ProdPgLooseID.find("span",class_="price js-price")
            
            ProdPgCibID = firstRow.find("td",id="complete_price")
            ProdPgCibPrice = ProdPgCibID.find("span",class_="price js-price")
            
            ProdPgNewID = firstRow.find("td",id="new_price")    
            ProdPgNewPrice = ProdPgNewID.find("span",class_="price js-price")

            if self.condition == "cib": return [ProdPgCibPrice.get_text().strip(),url]
            elif self.condition == "loose": return [ProdPgLoosePrice.get_text().strip(),url]
            elif self.condition == "new": return [ProdPgNewPrice.get_text().strip(),url]
            else: print("Please input a correctly syntaxed game condition")


g = Game("Pokemon Platinum","nintendo DS","cib","")
g.show()
print(g.getGamePrice())
