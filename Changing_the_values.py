import pandas as pd
import re
data = pd.read_csv('pokemon.csv', index_col=[0])
print(data)
data['Total'] = data.iloc[:,3:9].sum(axis=1)
# Now changing the value of Fire to Flamer
# Where Type 1 is Fire

data.loc[data['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
print(data)
print(data.loc[data['Legendary']=='True'])
print("After condition")
data.loc[data['Type 1']== 'Flamer', 'Legendary'] =True
print(data)
print(data.columns)
data.loc[data['Total'] > 500, ['Generation','Legendary']] = 'Test Value'
print(data)
print(data.iloc[2])
# To change individual value of multiple columns
data.loc[data['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1','Test 2']
print(data)
