import pandas as pd

# importing data from excek file
# To read Excel File install openpyxl library
# python3 -m pip install openpyxl

# importing data from excel file
data_xl = pd.read_excel(r'one.xlsx', index_col=[0])
"""for aa in pd.read_csv(r'pokemon.csv', chunksize = 5, index_col=False):
  #  if aa.loc[aa['Type 1'] == 'Fire']:
    print(" 5 Row.\n")
    print(aa)"""

#print(data_xl.sort_values('Name', ascending=False))
#one =data_xl.loc[loc['Name', 'Type 1']== '']
#one = data_xl.loc[data_xl['Type 1'] == 'Fire']
#print(one)
two = data_xl.sort_values('Type 1')
three = data_xl.sort_values(['Type 1', 'HP'])
#print(two)
#print(three)
"""two.to_csv('sortone.csv', sep='\t')
three.to_csv('sortthree.csv', sep='\t')
new=two[0:-1]+three[0:-1]
print(new)
new.to_csv('last.csv', sep='\t')"""
# Sorting
aabb=data_xl.sort_values(['Type 1', 'HP'], ascending=[1,0])
print(aabb)
four = data_xl.sort_values(['Name', 'HP'], ascending=[1,1])
four =four.reset_index(drop =True)
"""for i in four.iterrows():
    print(i)"""
print(four)
