import csv

class CSV_Writer:

    def __init__(self, write_path, priceDict):
        self.write_path = write_path
        self.priceDict = priceDict

    def writePricesToCSV(self): # write existing dictionairy and prices to a new CSV
        
        with open(self.write_path, 'w', newline='') as new_file:
            csv_writer = csv.writer(new_file)
            csv_writer.writerow(["Console", "Title", "Condition", "Current Price"])

            for row in prices:
                csv_writer.writerow([row["Console"], row["Title"], row["Condition"], row["Current Price"]])  