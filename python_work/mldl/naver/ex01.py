import pandas as pd
import re
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('ratings_train.txt',sep='\t')
print(data.head(3))
# print(data['label'].value_counts())

# print(data['document'][:10])

data = data.fillna(' ')
data['document'] = data['document'].apply( lambda x: re.sub(r'\d+',' ',x))

# print(data['document'][:10])

data.drop('id',axis=1,inplace=True)
print(data.head(3))

okt = Okt()
def tw_tokenizer(text):
    # 입력 인자로 들어온 text 를 형태소 단어로 토큰화 하여 list 객체 반환
    tokens_ko = okt.morphs(text)
    return tokens_ko

print(tw_tokenizer('한글로 들어온걸 토큰화 해준다'))

tfidf = TfidfVectorizer(tokenizer=tw_tokenizer,ngram_range=(1,2),max_df=0.9,min_df=3)
tfidf.fit(data['document'])
tfidf_matrix_train  = tfidf.transform(data['document'])

print(tfidf_matrix_train[:10])

import pickle

with open('tfidf.pickle','wb') as fw:
    pickle.dump(tfidf,fw)

with open('tfidf_matrix_train.pickle','wb') as fw:
    pickle.dump(tfidf_matrix_train,fw)







