import csv
from Archive.IndividualGamePricer import Game

class convertToDict:
    
    def __init__(self, read_path, write_path):
        self.read_path = read_path
        self.write_path = write_path

    def dictReaderCSV(self): # Convert the read_CSV into a Dictionary and Return
        
        with open(self.read_path, 'r') as csv_file:
            sample = csv_file.read(10)
            has_header = csv.Sniffer().has_header(sample)

        if has_header == True:

            with open(self.read_path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                for line in csv_reader:
                    print(dict(line))

        else: print("Please add a header to your data in the first row")

    

    def dictWriterCSV(self): 
        
        game_count = 0
        total_value = float(0)

        with open(self.read_path,'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            with open(self.read_path, 'w', newline = '') as new_file:
                columns = ["Console","Title","Condition","Current Price"]
                csv_writer = csv.DictWriter(new_file, fieldnames = columns)
                csv_writer.writeheader()

                for row in csv_reader: 
                    #(1) for each dictionary/row, define them as Game objects
                    g = Game("Title","Console","Condition") #why cant i define Game here?
                    game_count += 1
                    
                    for row in csv_reader:
                        csv_writer.writerow([row["Console"],row["Title"],row["Condition"],row["Current Price"]])

                print(f'You have {game_count} games in your collection!')
                     
# row["Current Price"] = g.getGamePrice()
# row["Current Price"].append(g)

# Notes from 1/7 - Trying to understand why my CSV writer is not writing correctly^

gameExample = Game("Pokemon Diamond","nintendo DS","cib")
gameExample.show() 
print(gameExample.getGamePrice())

testReadPath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 1" + ".csv"
testWritePath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 3" + ".csv"

listOfGame = ["Super Smash Bros. Melee", "World of Warcraft", "Call of Duty: Modern Warfare", "Super Smash Bros. Melee [Best Seller]"]
priceDictList = []

# Notes from 1/20 - Writing out what next steps I need to do, below. 
# currently working from Convert_Row_of_CSV... File

# I think i need to (1) define the first Dictionary/row in the CSV as a Game object.
# (2) Append the getGamePrice return value to the 'Current Price' key on that Game object
#  Then (3) loop through each Dictionary/row in the CSV
# (4) write each dictionary/row into a new CSV

readExample = convertToDict(testReadPath, testWritePath)
readExample.dictReaderCSV()


# gameList = c.dictConverterCSV()

# print(gameList)

# priceDictList = []

# for game in gameList:
#     priceDictList.append(getGamePrice())

# c.writePricesToCSV()