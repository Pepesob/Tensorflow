from matplotlib import pyplot
from sklearn import linear_model, metrics
import numpy as np

f = [9.81, 19.62, 29.43, 39.24, 49.05, 58.86, 68.67, 78.48, 88.29]
uh = [0.2625, 0.44, 0.5875, 0.7225, 0.8525, 0.975, 1.1, 1.2125, 1.3325]

'''f_np = np.array(f).reshape(-1,1)
uh_np = np.array(uh).reshape(-1,1)
'''
pyplot.scatter(f,uh)


"""model = linear_model.LinearRegression(fit_intercept=True)
model.fit(f_np,uh_np)"""

pyplot.title("Zależność wydłużenia od przyłożonej siły (stal)")
pyplot.xlabel("Siła F[N]")
pyplot.ylabel("Wydłużenie Δl[mm]")
pyplot.grid()

"""print(model.coef_, model.intercept_)

pred = model.predict(f_np)


print(metrics.mean_squared_error(uh_np, pred))"""

pyplot.show()

