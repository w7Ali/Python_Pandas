# importing the pandas as pd
import pandas as pd

# importing data in 10 rows chunk size
# with the help of for loop


for data in pd.read_csv('pokemon.csv', chunksize=10, index_col=[0]):
    print(data)