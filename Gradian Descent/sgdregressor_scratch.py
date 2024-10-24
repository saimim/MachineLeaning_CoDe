# -*- coding: utf-8 -*-
"""SGDRegressor_scratch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1APZ35TrlWksNHNoMVKyjWQpeV4Mx71aY
"""

from sklearn.datasets import load_diabetes

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import time

x,y = load_diabetes(return_X_y=True)

print(x.shape)
print(y.shape)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=2)

reg = LinearRegression()
reg.fit(x_train,y_train)

print(reg.coef_)
print(reg.intercept_)

y_pred = reg.predict(x_test)

r2_score(y_test,y_pred)

class SGDRegressor:
  def __init__(self,epochs):
    self.coef_ = None
    self.intercept_=None
    self.epochs = epochs
    self.t0 = 5
    self.t1 = 50


  def learning_rate(self,t):
    return self.t0/(t + self.t1)

  def fit(self,x_train,y_train):
    self.intercept_ = 0
    self.coef_ = np.ones(x_train.shape[1])    #Have Confusion.........

    for i in range(self.epochs):
      for j in range(x_train.shape[0]):
        idx = np.random.randint(0,x_train.shape[0])

        lr=self.learning_rate(i*x_train.shape[0] +j)

        y_hat = np.dot(x_train[idx],self.coef_) + self.intercept_

        intercept_der = -2*(y_train[idx] - y_hat)
        self.intercept_ = self.intercept_ - (lr*intercept_der)

        coef_der = -2 * np.dot((y_train[idx]-y_hat),x_train[idx])
        self.coef_ = self.coef_ - (lr*coef_der)

    print(self.intercept_,self.coef_)
  def predict(self,x_test):
    return np.dot(x_test,self.coef_) + self.intercept_

sgd = SGDRegressor(epochs=1000)

start = time.time()
sgd.fit(x_train,y_train)
print("The fit time take is",time.time() - start)

y_pred = sgd.predict(x_test)

r2_score(y_test,y_pred)

# #learning schedule
# t0,t1 = 5,50
# def learning_rate(t):
#   return t0/(t + t1)

# for i in range(epochs):
#   for j in range(x_train.shape[0]):
#     lr=learning_rate(i*x_train.shape[0] +j)

'''
learning rate will be:

1. constant
2. optimal
3. invscaling
'''