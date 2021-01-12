import pandas as pd
data = pd.read_excel(r'one.xlsx', index_col=[0])
# print(data)
# add new Column in excel file
print(data.columns)
data.info()
data['Total'] = data['HP'] + data['Attack'] + data['Defense'] + data['Sp. Atk'] + data['Sp. Def'] + data['Speed']
print(data.Total)
print(data)

data.drop(columns=['Total'])
print(data)
data['Total'] = data.iloc[:, 3:9].sum(axis=1)
des = data.describe()
cols = list(data.columns)
print(cols)
# Rearrange
aaaaa=data[cols[0:3] + cols[4:10] + [cols[-1]]+ [cols[-2]]]
print(data.iloc[1])
print(aaaaa.iloc[1])