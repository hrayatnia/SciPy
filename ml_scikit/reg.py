import numpy as np
import matplotlib.pyplot as mpl
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model
from sklearn.datasets.samples_generator import make_regression
X, y = make_regression(n_samples=100, n_features=2, n_informative=1,\
random_state=0, noise=50)
X_train, X_test = X[:80], X[-20:]
y_train, y_test = y[:80], y[-20:]
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
print(regr.coef_)
X1 = np.array([1.2, 4])
print(regr.predict(X1))

fig = mpl.figure(figsize=(8, 5))
ax = fig.add_subplot(111, projection='3d')
   #ax = Axes3D(fig)
# Data
ax.scatter(X_train[:,0], X_train[:,1], y_train, facecolor='#00CC00')
ax.scatter(X_test[:,0], X_test[:,1], y_test, facecolor='#FF7800')
# Function with coefficient variables
coef = regr.coef_
line = lambda x1, x2: coef[0] * x1 + coef[1] * x2
grid_x1, grid_x2 = np.mgrid[-2:2:10j, -2:2:10j]
ax.plot_surface(grid_x1, grid_x2, line(grid_x1, grid_x2),
                alpha=0.1, color='g')
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.zaxis.set_visible(False)
fig.savefig('scikit_learn_regression.pdf', bbox='tight')
print(regr.score(X_test, y_test))