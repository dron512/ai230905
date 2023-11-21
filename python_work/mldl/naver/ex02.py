import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

data = pd.read_csv('ratings_train.txt',sep='\t')

with open('tfidf_matrix_train.pickle','rb') as f:
    matrix = pickle.load(f)

lg_clf = LogisticRegression(random_state=0, solver='liblinear')

params = { 'C': [1 ,3.5, 4.5, 5.5, 10 ] }
grid_cv = GridSearchCV(lg_clf , param_grid=params , cv=3 ,scoring='accuracy', verbose=1 )
grid_cv.fit(matrix , data['label'] )
print(grid_cv.best_params_ , round(grid_cv.best_score_,4))

best_estimator = grid_cv.best_estimator_

import pickle
with open('saved_model.pickle','wb') as fw:
    pickle.dump(best_estimator,fw)