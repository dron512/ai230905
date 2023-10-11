import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

'''
data = pd.read_csv('data.csv')
print(data)

# data = data.T
# print(data)

print(data['a'])
print(data['b'])

plt.plot(data['a'],data['b'])
plt.savefig('a.png')
'''
matplotlib.rcParams['font.family'] = 'Malgun Gothic' # Windows
matplotlib.rcParams['font.family'] = 'BM YEONSUNG' # Windows
matplotlib.rcParams['font.family'] = 'BareunBatangPro' # Windows
matplotlib.rcParams['font.family'] = 'tvN Enjoystories' # Windows
matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF' # Windows

# matplotlib.rcParams['font.family'] = 'AppleGothic' # Mac
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

x = [10,20,60]
y = [30,3,90]

plt.plot(x,y)
plt.title('한글그래프')
plt.show()
# plt.savefig('b.png')

import matplotlib.font_manager as fm
fm.fontManager.ttflist # 사용 가능한 폰트 확인
for i in fm.fontManager.ttflist:
    print(str.encode(i.name,'utf-8'))












