from sklearn import linear_model
import sklearn
import numpy as np
from matplotlib import pyplot


def fun(x):
    return 3.9267*x


x_train = [0.213,
0.213,
0.213,
0.286,
0.286,
0.286,
0.342,
0.342,
0.342,
0.405,
0.405,
0.405,
0.45,
0.45,
0.45,
0.506,
0.506,
0.506,
]

y_train = [
0.857013,
0.911548,
0.832656,
1.112498,
1.095686,
1.150256,
1.390631,
1.368315,
1.385329,
1.597064,
1.605289,
1.619256,
1.73054,
 1.678968,
 1.747023,
 2.055639,
 2.05134,
 2.042756,
]

x1 = [i*0.01 for i in [104.1, 97.9, 91, 83.5, 72.2, 65.1, 59, 53.2, 46.7, 40.1, 35.4, 29.9, 26.6, 17.9, 11.2]]
y1 = [4.18, 3.96, 3.63, 3.38, 2.89, 2.62, 2.37, 2.13, 1.87, 1.60, 1.42, 1.20, 1.06, 0.72, 0.45]

x = np.array(x_train).reshape(-1,1)
y = np.array(y_train).reshape(-1,1)

x2 = np.array(x1).reshape(-1,1)
y2 = np.array(y1).reshape(-1,1)


linear = linear_model.LinearRegression()
linear.fit(x, y)

pred = linear.predict(x)

print(linear.coef_)

t = [fun(v) for v in x_train]

print(sklearn.metrics.mean_squared_error(y, pred))

heh =  [0.92575,0.95475,0.9125,1.05475,1.04675,1.0725,1.17925,1.16975,1.177,1.26375,1.267,1.2725,1.3155,1.29575,1.32175,1.43375,1.43225,1.42925]


pyplot.plot(x_train,y_train,'ro')
pyplot.plot(x_train, [fun(c) for c in x_train])
pyplot.title("Wykres zlinearyzowany okresu od długości wahadła")
pyplot.xlabel('Długość wahadła l[m]')
pyplot.ylabel('Okres wahadła T^2[s^2]')
pyplot.grid()
pyplot.show()
