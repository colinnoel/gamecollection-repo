
from bs4 import BeautifulSoup
import requests
import csv

class GameCollection:
    
    def __init__(self, read_path, write_path):
        self.read_path = read_path
        self.write_path = write_path

    def readCSV(self): # Read the Game Collection in a simple format
        
        with open(self.read_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0

            for line in csv_reader:
                print(line)
                line_count += 1
            game_count = line_count
            print(f"You have {line_count} games in your collection!")


    def dictReaderCSV(self): # Convert the read_CSV into a Dictionary and Print
        
        with open(self.read_path, 'r') as csv_file:
            sample = csv_file.read(10)
            has_header = csv.Sniffer().has_header(sample)

        if has_header == True:

            with open(self.read_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                for line in csv_reader:
                    print(dict(line))

        else: print("Please add a header to your data in the first row")

    def dictConverterCSV(self): # Convert the read_CSV into a Dictionary and Return
        
        with open(self.read_path, 'r') as csv_file:
            sample = csv_file.read(10)
            has_header = csv.Sniffer().has_header(sample)

        if has_header == True:

            with open(self.read_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                for line in csv_reader:
                    return dict(line)

        else: print("Please add a header to your data in the first row")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getGamePrice(title, console, condition):
    consoleDict = {"nintendo ds":"G5","nintendo 3ds":"G39","nintendo switch":"G59",
                    "xbox 360":"G10","playstation 4":"G53","playstation 3":"G12"
                    ,"playstation 2":"G7","playstation 1":"G6","nintendo wii":"G11",
                    "nintendo wii U":"G47","gameboy advance":"G1","nintendo 64":"G4"}
    consoleID = consoleDict[console.lower()]
    
    
    baseURL = "https://www.pricecharting.com/search-products?q="
    title_query = title.lower().replace(" ", "+")
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

        if condition == "cib": return cibPrice.get_text()
        elif condition == "loose": return loosePrice.get_text()
        elif condition == "new": return newPrice.get_text()
        else: print("Please input a correctly syntaxed game condition")
    
    else:
        ProdPgLooseID = firstRow.find("td",id="used_price")
        ProdPgLoosePrice = ProdPgLooseID.find("span",class_="price js-price")
        
        ProdPgCibID = firstRow.find("td",id="complete_price")
        ProdPgCibPrice = ProdPgCibID.find("span",class_="price js-price")
        
        ProdPgNewID = firstRow.find("td",id="new_price")    
        ProdPgNewPrice = ProdPgNewID.find("span",class_="price js-price")

        if condition == "cib": return ProdPgCibPrice.get_text().strip()
        elif condition == "loose": return ProdPgLoosePrice.get_text().strip()
        elif condition == "new": return ProdPgNewPrice.get_text()
        else: print("Please input a correctly syntaxed game condition")
        
    

c = GameCollection(r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 1" + ".csv", r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 2" + ".csv")
gameList = c.dictConverterCSV()

print(gameList)

priceDictList = []


for game in gameList:
    priceDictList.append(getGamePrice())

# c.writePricesToCSV()




