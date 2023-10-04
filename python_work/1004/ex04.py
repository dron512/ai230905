import pandas as pd
from ipython_genutils.py3compat import input

data = pd.read_excel('a.xlsx')

print(data,end='\n\n')
data.set_index('이름', inplace=True)
print(data)

# print(data['이름'])



# data.to_csv('a.csv')
# data.to_csv('a.txt',sep='\t')