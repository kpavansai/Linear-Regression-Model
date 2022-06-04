# Import libraries
import numpy as np
form numpy import array
from numpy.linalg import inv
import matplotlib.pyplot as plt

# data



class LinearRegression():
  def __init__(self):
    """Initialize the variables co-eff and pred"""
    self.coef = None
    self.pred = None
    
  def fit(self, X, y):
    self.X = X
    self.y = y
 
    if len((self.X).shape) == 1:
      self.X = (self.X).reshape(-1,1)
      
    self.coef = inv(self.X.T.dot(self.X)).dot(self.X.T).dot(self.y)
    
  def predict(self):
    """Predict the y values using the coef calculated above"""
    if len(self.X).shape) == 1:
      self.X = (self.X).reshape(-1, 1)
      
    self.pred = self.X.dot(self.coef)
    return self.pred
  
  def plt_prediction(self):
    """Generate Some Plots"""
    
    plt.scatter(self.X, self.y)
    plt.plot(self.X, self.pred, color = "red")
    plt.show

    
    
# Run the above code

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

mylinearreg = LinearRegression()
mylinearreg.fit(X,y)
print(mylinearreg.predict())
