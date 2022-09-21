import pandas as pd

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things

df = pd.read_csv('C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\Game Collection Example 3.csv', delimiter=',')

# or export it as a list of dicts
dicts = df.to_dict('records')

print(dicts)