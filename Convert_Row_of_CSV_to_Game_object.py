import csv
from GamePricer import Game

testReadPath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 3" + ".csv"
testWritePath = r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 3" + ".csv"


game_count = 0
total_value = float(0)


with open(testReadPath,'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader: 
        print(dict(row))

    for row in csv_reader: 
    #     #(1) for each dictionary/row, define them as individual Game objects
        g = Game(row["Title"],row["Console"],row["Condition"], 0) 
        game_count += 1
    #     #(2) Append the getGamePrice return value to the 'Current Price' key on that Game object
        ["Current Price"].append(g.getGamePrice(["Title"],["Console"],["Condition"]))
        print(g)

    #     #(2)Loop through each Dictionary/row in the CSV
        # for row in csv_reader: 
        #     csv_writer.writerow([row["Console"],row["Title"],row["Condition"],row["Current Price"]])


    # print(f'You have {game_count} games in your collection!')


# I think i need to (1) define the first Dictionary/row in the CSV as a Game object.
# (2) Append the getGamePrice return value to the 'Current Price' key on that Game object
# Then (3) loop through each Dictionary/row in the CSV
# (4) write each dictionary/row into a new CSV