# importing the pandas library
import pandas as pd
data = pd.read_csv('pokemon.csv', index_col=[0])

# Filtering the data
fire_data = data.loc[data['Type 1']== 'Fire']
print(fire_data)
fire_poison = data.loc[
    (data['Type 1']== 'Grass')
    &
    (data['Type 2']== 'Poison')
]
print(fire_poison)
count=len(fire_poison)
print(count)
condition = data[
    (
        data['Type 1'] == 'Grass'
    )
    &
    (
        data['Type 2'] == 'Poison'
    )
    &
    (
        data['HP'] > 70
    )
]
print("Applying three condition in single dataframe to sorting the data")
print(condition)
