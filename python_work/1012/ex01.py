import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False  # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

x1 = [1, 2, 3]
y1 = [4, 8, 6]

x2 = [4, 3, 5]
y2 = [1, 9, 4]

x3 = [3, 7, 9]
y3 = [1, 3, 11]

plt.plot(x1, y1, label='aa', linestyle='--')
plt.plot(x2, y2, label='bb', linestyle='-.')
plt.plot(x3, y3, label='cc')
plt.title('여러데이터출력')

plt.legend(ncol=3)
plt.show()
