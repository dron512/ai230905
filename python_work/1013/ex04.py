import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# import matplotlib.image as mpimg
# background_image_path = 'bb.png'  # 이미지 파일 경로를 수정하세요.

# background_image = mpimg.imread(background_image_path)

matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../a.xlsx')

values = [30, 25, 20, 13, 10, 2]
explode = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

plt.figure(figsize=(11,7))
plt.title('언어별 선호도')
plt.pie( values, labels=data['SW특기'].dropna() ,
         autopct='%.1f%%',startangle=90,explode=explode)
plt.legend(loc=(1.2,0.3))
# plt.imshow(background_image)
plt.show()
