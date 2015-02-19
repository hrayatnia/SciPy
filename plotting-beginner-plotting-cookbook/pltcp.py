import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt
ax = plt.axes(polar = True)
theta = np.linspace(0, 2 * np.pi, 8, endpoint = False)
radius = .25 + .75 * np.random.random(size = len(theta))
points = np.vstack((theta, radius)).transpose()
plt.gca().add_patch(patches.Polygon(points, color = '.75'))
plt.show()