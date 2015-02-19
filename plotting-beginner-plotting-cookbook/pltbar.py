import numpy as np
import matplotlib.pyplot as plt
data = [[5., 25., 50., 20.],
 [4., 23., 51., 17.],
 [6., 22., 52., 19.]]
X = np.arange(4)
plt.bar(X + 0.00, data[0], color = 'b', width = 0.25)
plt.bar(X + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(X + 0.50, data[2], color = 'r', width = 0.25)
plt.show()