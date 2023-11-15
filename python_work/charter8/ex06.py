from sklearn.datasets import fetch_20newsgroups
import pandas as pd

news_data = fetch_20newsgroups(subset='all',random_state=156)

print(news_data.keys())

print('target 클래스의 값과 분포도 \n',
      pd.Series(news_data.target).value_counts().sort_index())
print('target 클래스의 이름들 \n',news_data.target_names)

print(news_data.target_names[8])

print(news_data.data[0])
print(news_data.target[0])

print(news_data.data[1])
print(news_data.target[1])
