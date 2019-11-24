# coding=utf-8

################################
# 150114022 - Oğuzhan BÖLÜKBAŞ #
################################

import math
import numpy as np
import pylab as plt

N = 100

# 8.1-)
mean = np.array([0, 0]).T  # To generate desired mean
p = (1 / (2 * math.pi)) ** ((-1 * (np.eye(2) * np.eye(2))) / 2)  # Identity covariance matrix
x1, x2 = np.random.multivariate_normal(mean, p, N).T  # To generate 2D Gaussian Dist.

ax = plt.subplot(111)  # To use limitations
ax.set_ylim(-5, 5)  # To limit y axes
ax.set_xlim(-5, 5)  # To limit x axes
ax.plot(x1, x2, 'o')  # To plot result
plt.title("Plot 1")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()  # To display the result

# 8.2-)
mean = np.array([1, -1]).T  # To generate desired mean
p = (1 / (2 * math.pi)) ** ((-1 * (np.eye(2) * np.eye(2))) / 2)  # Identity covariance matrix
x1, x2 = np.random.multivariate_normal(mean, p, N).T  # To generate 2D Gaussian Dist.

ax = plt.subplot(111)  # To use limitations
ax.set_ylim(-5, 5)  # To limit y axes
ax.set_xlim(-5, 5)  # To limit x axes
ax.plot(x1, x2, 'o')  # To plot result
plt.title("Plot 2")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()  # To display the result

# 8.3-)
mean = np.array([0, 0]).T  # To generate desired mean
p = np.array([[2, 0], [0, 2]])  # Identity covariance matrix
x1, x2 = np.random.multivariate_normal(mean, p, N).T  # To generate 2D Gaussian Dist.

ax = plt.subplot(111)  # To use limitations
ax.set_ylim(-5, 5)  # To limit y axes
ax.set_xlim(-5, 5)  # To limit x axes
ax.plot(x1, x2, 'o')  # To plot result
plt.title("Plot 3")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()  # To display the result

# 8.4-)
mean = np.array([0, 0]).T  # To generate desired mean
p = np.array([[2, 1], [1, 2]])  # Identity covariance matrix
x1, x2 = np.random.multivariate_normal(mean, p, N).T  # To generate 2D Gaussian Dist.

ax = plt.subplot(111)  # To use limitations
ax.set_ylim(-5, 5)  # To limit y axes
ax.set_xlim(-5, 5)  # To limit x axes
ax.plot(x1, x2, 'o')  # To plot result
plt.title("Plot 4")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()  # To display the result

# 8.5-)
mean = np.array([0, 0]).T  # To generate desired mean
p = np.array([[2, -1], [-1, 2]])  # Identity covariance matrix
x1, x2 = np.random.multivariate_normal(mean, p, N).T  # To generate 2D Gaussian Dist.

ax = plt.subplot(111)  # To use limitations
ax.set_ylim(-5, 5)  # To limit y axes
ax.set_xlim(-5, 5)  # To limit x axes
ax.plot(x1, x2, 'o')  # To plot result
plt.title("Plot 5")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()  # To display the result
