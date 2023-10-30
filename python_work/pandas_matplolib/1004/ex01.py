import pandas as pd

data = pd.Series([10,20,30,40])
print(data)

data = pd.Series([10,20,30,40],index=['aa','bb','cc','dd'])
print(data)

'''
    날씨 조는 데이터를 가지고 오면 판다스 라이브러리를 이용해서 
    엑셀에 데이터를 저장하는걸로 만듭니다.
'''

