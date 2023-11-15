from sklearn.datasets import fetch_20newsgroups

news_data = fetch_20newsgroups(subset='all',random_state=156)

# subset='train'으로 학습용(Train) 데이터만 추출, remove=('headers', 'footers', 'quotes')로 내용만 추출
train_news= fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), random_state=156)
X_train = train_news.data
y_train = train_news.target
print(type(X_train))

# subset='test'으로 테스트(Test) 데이터만 추출, remove=('headers', 'footers', 'quotes')로 내용만 추출
test_news= fetch_20newsgroups(subset='test',remove=('headers', 'footers','quotes'),random_state=156)
X_test = test_news.data
y_test = test_news.target
print('학습 데이터 크기 {0} , 테스트 데이터 크기 {1}'.format(len(train_news.data) , len(test_news.data)))

print(test_news.data[10])
print(test_news.target[10])
print(news_data.target_names[3])

print('---------------------')
print(test_news.data[20])
print(test_news.target[20])
print(news_data.target_names[6])

from sklearn.feature_extraction.text import CountVectorizer

# Count Vectorization으로 feature extraction 변환 수행.
cnt_vect = CountVectorizer()

cnt_vect.fit(X_train)
X_train_cnt_vect = cnt_vect.transform(X_train)

# 학습 데이터로 fit( )된 CountVectorizer를 이용하여 테스트 데이터를 feature extraction 변환 수행.
X_test_cnt_vect = cnt_vect.transform(X_test)

print(X_train_cnt_vect[10])
print('---------------------')
print(X_test_cnt_vect[20])
print('학습 데이터 Text의 CountVectorizer Shape:',X_train_cnt_vect.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

# LogisticRegression을 이용하여 학습/예측/평가 수행.
lr_clf = LogisticRegression(solver='liblinear')
lr_clf.fit(X_train_cnt_vect , y_train)
pred = lr_clf.predict(X_test_cnt_vect)
print('CountVectorized Logistic Regression 의 예측 정확도는 {0:.3f}'.format(accuracy_score(y_test,pred)))

test_data = '''
Title: "Passion and Precision: The Life of a Soccer Athlete"
Article:
Soccer is a sport where passion and precision coexist, and athletes adorn the field with exceptional skills and teamwork. In this article, we delve into the daily life, training, and moments of true passion that define the journey of a soccer athlete.
Morning Training and Physical Conditioning:
A soccer player's day begins early, with a focus on physical conditioning and training. Early workouts are essential for achieving peak performance on the field, often emphasizing speed, strength, and balance.
Tactical Meetings and Team Building:
Following training, tactical meetings take place with the team. Each player understands their role and engages in discussions to foster harmony with teammates. Soccer places importance not only on individual abilities but also on teamwork, making team building a crucial component.
Game Day Tension and Passion:
On game day, players are filled with anticipation and tension. Their eyes reflect a desire for victory and a deep love for the game. Once the match begins, they strive for victory through strategic moves and precise passes.
Interaction with Fans:
Soccer players value communication with their fans. After the game, they take time to interact with fans, expressing gratitude and capturing moments through photographs. Fan support serves as a tremendous source of motivation, and players always extend their appreciation.
Rest and Recharge:
After the game, rest is crucial. Players take time to relax and recharge their energy for the next match. Quality time with family or engaging in hobbies plays a vital role in this stage.
The life of a soccer player is an intriguing journey resulting from dedication and passion. Through their exceptional skills, commitment, and collaboration with teammates, soccer becomes a truly special experience for these athletes.
'''

# 글을 숫자 형태로 바꾸기...
test_data = cnt_vect.transform([test_data])

predValue = lr_clf.predict(test_data)
print(predValue)
print(news_data.target_names[predValue])