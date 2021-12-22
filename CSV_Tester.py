
import csv

currentCSVPath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 1" + ".csv"

endCSVPath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 2" + ".csv"

def readGameCollectionCSV(path):
    
    with open(currentCSVPath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            print(line)

def writePricesToCSV(path, prices):

    with open(endCSVPath, 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(["System", "Title", "Condition", "Current Market Value"])

        for line in prices:
            csv_writer.writerow([row["System"], row["Title"], row["Condition"], row["Current Market Value"]])

readGameCollectionCSV(currentCSVPath)