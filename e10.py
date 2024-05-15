""" write a python program to create pandas dataframe using dictionaries and apply the following operations-
a) change the column and index name
b) renaming a column
c) get n-largest value from a particular column in pandas dataframe
d) apply uppercase to a column """

import pandas as pd


data = {
  "alNum":['one', 'two', 'three'],
  "2x": range(2, 7, 2)
}

df = pd.DataFrame(data, index=range(1, 4))

df = df.rename(index={1:"a"})
print(df, '\n')

df.rename(index = {"a":1}, columns={"2x":"twice"}, inplace=True)
print(df, '\n')

max = df.nlargest(1, ['twice'])
print(max, '\n')

df['alNum'] = df['alNum'].str.upper()
print(df, '\n')