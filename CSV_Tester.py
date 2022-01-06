
import csv

currentCSVPath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 1" + ".csv"

endCSVPath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 2" + ".csv"

def readCSV(path):
    
    with open(currentCSVPath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file) #delimiter is implied to be ','
        line_count = 0

        for line in csv_reader:
            print(line)
            line_count += 1

        print(f"You have {line_count} games in your collection!")

def writePricesToCSV(path, prices):

    with open(endCSVPath, 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(["System", "Title", "Condition", "Current Market Value"])

        for line in prices:
            csv_writer.writerow([row["System"], row["Title"], row["Condition"], row["Current Market Value"]])

readCSV(currentCSVPath)