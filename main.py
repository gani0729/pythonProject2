import pandas as pd

# read the first file
df1 = pd.read_csv('housing1.csv')

# read the second file
df2 = pd.read_csv('housing2.csv')

# concatenate the two dataframes
df = pd.concat([df1, df2])

# print the concatenated dataframe
print(df)



