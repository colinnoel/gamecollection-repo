import pandas as pd

url = 'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 3" + ".csv"


# Read the CSV into a pandas data frame (df)
df = pd.read_csv(url, delimiter=',')

# export it as a list of dicts
dicts = df.to_dict('records')
print(dicts)

