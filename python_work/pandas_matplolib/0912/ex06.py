import numpy as np
from sklearn.neighbors import KNeighborsRegressor

alist = [1,2,3,4]
blist = [5,6,7,8]

npalist = np.array(alist)
npblist = np.array(blist)

print(alist+blist)
print(npalist+npblist)

print(len(alist))
print(npalist.shape)

x = [[1,3],[2,5],[3,7],[4,9],[5,10],[6,22],[7,33],[8,44],[9,55],[10,33]]
y = [15,21,33,42,56,63,74,87,93,105]

knr = KNeighborsRegressor()
knr.fit(x,y)

pred = knr.predict([[3.5,8],[5.5,11]])
print(pred)