import pandas as pd

data = pd.read_excel('a.xlsx')
# print(data)

print(data.head())
print(data.describe())

print(data.info())

# data.dropna('과학',inplace=True)

'''
pandas 
'''