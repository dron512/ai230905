import pandas as pd

data = pd.read_excel('a.xlsx')
print(data)

data['총합'] = data['국어']+data['영어']+data['수학']+data['과학']
print(data)

data['학교'] = data['학교']+'등학교'
print(data)

data['결과'] = 'Fail'
print(data)

test = data['총합']>300
print(test)

data.loc[test,'결과'] = 'Pass'
print(data)

data = data.drop(columns ='총합')
print(data)

data.loc[len(data)] = ['홍길동','대구고등하교',100,20,30,40,50,60,'Java','Pass']
print(data)
data.loc[len(data)] = ['홍길동','대구고등하교',100,20,30,40,50,60,'Java','Pass']
print(data)
data.loc[len(data)] = ['홍길동','대구고등하교',100,20,30,40,50,60,'Java','Pass']
print(data)
data.loc[len(data)] = ['홍길동','대구고등하교',100,20,30,40,50,60,'Java','Pass']
print(data)

# df = data._append(
#     ['홍길동','대구고등하교',100,20,30,40,50,60,'Java','Pass']
#     , ignore_index=True)
# print(df)















