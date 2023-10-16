import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

colors = ['#ff0000','#00ff00','#0000ff']

# plt.barh([1,2,3],[180,190,200])
plt.bar([0.7, 1.2, 1.7], [180, 190, 200], color=colors, alpha=0.5,width=0.3)
for x,y in zip([0.7, 1.2, 1.7],[190, 200, 210]):
    plt.text(x,y,y-10)

plt.bar([1, 1.5, 2], [150, 160, 170], width=0.3)

plt.bar([1.2, 1.7, 2.3], [-50, -70, -90], width=0.3)

plt.plot([1, 2, 3], [210, 300, 290],
         linewidth=10, c='#ff0000', marker='o',
         markersize=40, markerfacecolor='red', markeredgecolor='green')

# plt.ylim(130,300)

plt.title('바그래프')
plt.show()
