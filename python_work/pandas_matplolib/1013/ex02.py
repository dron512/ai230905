import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.image as mpimg
background_image_path = 'bb.png'  # 이미지 파일 경로를 수정하세요.

background_image = mpimg.imread(background_image_path)

# background_image.resize()

matplotlib.rcParams['font.family'] = 'Gmarket Sans TTF'  # Windows
matplotlib.rcParams['font.size'] = 15  # 글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False

data = pd.read_excel('../a.xlsx')

plt.bar(data['이름'],data['국어'],label='국어')
plt.bar(data['이름'],data['영어'],bottom=data['국어'],label='영어')
plt.bar(data['이름'],data['수학'],bottom=data['국어']+data['영어'],label='수학')

plt.plot(data['이름'],data['키'])

plt.legend()

plt.xticks(rotation=60)
plt.imshow(background_image)
plt.show()