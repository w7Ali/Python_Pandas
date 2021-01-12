# importing the data
import pandas as pd
import re

data = pd.read_csv('pokemon.csv', index_col=[0])

# Aggregate Function (Group by)
one = data.groupby(['Type 1']).mean()
print("It will give average \n")
print(one)
two = data.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)
print("Highest Defense \n")
print(two)
new = data.loc[data['Name'].str.contains('^pika[a-z]*', flags=re.I, regex=True)]
print(new)
print(data.groupby(['Generation']).mean().sort_values('Attack', ascending=False))
data_plt = data.groupby(['Type 1']).sum().sort_values('Type 1', ascending=1)
print(data_plt)
print(data.groupby(['Type 1']).sum())
# Let's count how many pokemon in every group
print(data.groupby(['Type 1']).count().sort_values('Type 1', ascending=True))
data['count'] = 1
print(data)
new=data['count'] = data.groupby(['Type 1']).count()['count']
print(new)
data['new_con'] = 1
print(data.groupby(['Type 1','Type 2']).count()['new_con'])
