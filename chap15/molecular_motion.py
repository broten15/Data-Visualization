import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

# plots walks
plt.plot(rw.x_values, rw.y_values, linewidth=1)
#plots start and stop points
plt.scatter(rw.x_values[0], rw.y_values[0], c='green', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=50)

# Removes axis
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()