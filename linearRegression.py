# Importing libraries
import numpy as np
from numpy import array
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Data
data = array([
   [0.05, 0.12],
   [0.18, 0.22],
   [0.31, 0.35],
   [0.42, 0.38],
   [0.5, 0.49],
   ])
#separate out X and y and reshape
X = data[:,0]
y = data[:,-1]
X = X.reshape(-1,1)
y = y.reshape(-1,1)#let's try to calculate coef using linear algebra, to predict the y #which is = coef*X (not including the intercept at this moment)coef_ = inv(X.T.dot(X)).dot(X.T).dot(y)
yhat = X.dot(coef_)#Finally let's plot the dataplt.scatter(X, y)
plt.plot(X, yhat, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
