import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = TfidfVectorizer(ngram_range=(2,2))
X = vectorizer.fit_transform(corpus)
print(X)
print(X.shape)

print(vectorizer.vocabulary_)
## 출력
print(vectorizer.get_feature_names_out())
data = pd.DataFrame(X.toarray(),
             columns=list(vectorizer.get_feature_names_out()))
print(data)