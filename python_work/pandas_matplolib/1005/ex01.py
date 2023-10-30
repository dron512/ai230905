import pandas as pd

data = pd.read_excel('data.xlsx')
print(data)
test = data['키']>185
print(test)
print(data[data['키']>185])
print(data.loc[test,['국어','영어']])

test = data['이름'].str.startswith('송')

print(data[test])

test = data['이름'].str.contains('태')
print(data[test])

test = data['SW특기'].isin(['Python','Java'])
print( data[test] )
