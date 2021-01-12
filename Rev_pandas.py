import pandas as pd

# importing data from excek file
# Before importing the excel file you need to install
# openpyxl libaray
# python3 -m pip install openpyxlf
data_xl = pd.read_excel(r'one.xlsx', index_col=False)
print(data_xl)
# Read first rows
print(data_xl.columns)
print(data_xl.Name)
print(data_xl[['Name', 'Type 1']])
aa = data_xl[['Name', 'Type 1']]

# [Row x Column] Slicing
aab=data_xl.iloc[0:3, 0:5]
print("Iloc Function to access data")
print(aab)
print(data_xl)

# Accesing each row
for i, rowss in data_xl.iterrows():
    print(i,rowss)

for i, rows in data_xl.iterrows():
    if rows['Type 1'] == 'Fire':
        print(i, rowss)

# Describe
print(data_xl.describe())

a4 = data_xl.loc[data_xl['Type 1' ]== 'Fire']
print(a4)
