import csv

with open('C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\Game Collection Example 3.csv',newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)