import matplotlib.pyplot as plt
import matplotlib
import matplotlib.image as mpimg
background_image_path = 'aa.jpg'  # 이미지 파일 경로를 수정하세요.

background_image = mpimg.imread(background_image_path)


matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF' # Windows
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용 시, 마이너스 글자가 깨지는 현상을 해결

x = [150,200,400]
y = [300,30,500]

x2 = [30,50,70]
y2 = [10,3,110]

plt.figure(figsize=(15,5))
plt.plot(x,y,label='A데이터',linewidth=5,marker='X',markersize=30,markerfacecolor='red',markeredgecolor='green', alpha=0.3)
plt.plot(x2,y2,label='B데이터',marker='o')
plt.legend(loc='lower right')

plt.title('한글그래프',fontdict={'family':'BM YEONSUNG','size':50})
plt.xlabel('x축',color='red',loc='right')
plt.ylabel('y축',color='#ffcc00',loc='top')

plt.scatter(70,80)

plt.xticks([10,30,60])
plt.yticks([10,30,60])

plt.text(100,100,'안녕하세요',ha='center')
plt.text(500,1000,'안녕하세요',ha='center')

for elex,eley in zip(x,y):
    plt.text(elex,eley+10,f'[{elex},{eley}]',ha='center')

plt.imshow(background_image)
plt.show()
# plt.savefig('a.png')
# plt.close()













