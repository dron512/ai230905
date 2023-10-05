import pandas as pd
# import matplotlib.pyplot as plt

data = pd.read_excel('a.xlsx')
print(data)

# data = data.fillna('Java')
# 행삭제
# data = data.dropna()
# 컬럼삭제
# data = data.dropna(axis='columns')
# print(data)

# index 순서로 정렬해라
print(data.sort_index())
# 키 열로 순서를 정렬해라
print(data.sort_values('키'))
print(data.sort_values('키',ascending=False))

print(data['키'].sort_values())

data.replace({'북산고':'능남고'},inplace=True)
print(data)

data = data['SW특기'].str.lower()
print(data)


# plt.plot(data['국어'])
# plt.show()