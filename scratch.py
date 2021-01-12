import pandas as pd
import re
data = pd.read_csv('pokemon.csv', index_col=[0])
print(data)
# Filtering by string
new = data.loc[
    data['Name'].str.contains('Mega')
]
print(new)
# Reversing the condition by putting Tide (~) sign in front of condition
new_2 = data.loc[
    ~ data['Name'].str.contains('Mega')
]
print(new_2)
three = data.loc[
    data['Name'].str.contains('Fire|Grass', regex=True)
]
print(three)
four = data.loc[
    data['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)
]
print(four)
five = data.loc[
    data['Name'].str.contains('pi[a-z]*', flags=re.I, regex=True)
]
print(five)
# To bring it in front for filtering
six = data.loc[
    data['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)
]
print(six)