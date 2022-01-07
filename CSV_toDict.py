import csv
from GamePricer import Game
from typing import List, Dict

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

        with open(self.read_path,'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)


            with open(self.read_path, 'w', newline = '') as new_file:
                columns = ["Console","Title","Condition","Current Price"]
                csv_writer = csv.DictWriter(new_file, fieldnames = columns)
                csv_writer.writeheader()

                for row in csv_reader:
                    
                    # g = Game(row["Title"], row["Console"], row["condition"])
                    # row["Current Price"] = g.getGamePrice()
                    # row["Current Price"].append(g)
                    game_count += 1
                    csv_writer.writerow([row["Console"],row["Title"],row["Condition"],row["Current Price"]])

                print(f'You have {game_count} games in your collection!')
                     

                    

# Notes from 1/7 - Trying to understand why my CSV writer is not writing correctly^


c = convertToDict(r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 1" + ".csv", r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 2" + ".csv")
# c.dictReaderCSV()
c.dictWriterCSV()



# gameList = c.dictConverterCSV()

# print(gameList)

# priceDictList = []

# for game in gameList:
#     priceDictList.append(getGamePrice())

# c.writePricesToCSV()