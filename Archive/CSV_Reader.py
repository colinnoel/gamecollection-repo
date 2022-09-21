import csv


class CSV_Reader:
    
    def __init__(self, read_path):
        self.read_path = read_path


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



c = CSV_Reader(r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 3" + ".csv")

#c.readCSV()
c.dictReaderCSV()


# c.["Current Price"].append(Game.getGamePrice())