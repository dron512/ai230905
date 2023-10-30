import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../a.xlsx')

print(data)

plt.figure(figsize=(15,5))
plt.plot(data['이름'],data['키'],label='키')
plt.plot(data['이름'],data['국어'],label='국어')
plt.plot(data['이름'],data['영어'],label='영어')

plt.grid(axis='y',color='purple',alpha=0.3)
plt.legend(loc='upper right')

plt.savefig('a.png')