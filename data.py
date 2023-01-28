import pandas as pd
import random


dataframe= pd.read_csv('data/french_words.csv')


data = dataframe.to_dict(orient='records')
current = random.choice(data)
print(current['French'])