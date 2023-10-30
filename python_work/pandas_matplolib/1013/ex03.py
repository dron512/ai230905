import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../a.xlsx')

x = [i for i in range(8)]
print(x)

x = np.arange(8)
print(x)

x = x - 0.25
print(x)

plt.figure(figsize=(15,5))
plt.bar(x - 0.25, data['영어'], width=0.25)
plt.bar(x, data['국어'], width=0.25)
plt.bar(x + 0.25, data['수학'], width=0.25)

plt.xticks(x,data['이름'],rotation=60)
plt.show()
