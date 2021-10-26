#!/usr/bin/env python
# coding: utf-8

# ## Random walk
# 
# We simulate a simple random walk in $d$ dimensions. In a first implementation, the steps have a fixed length $\delta$ along each dimension. To improve the statistics, we simulate $M$ independent walks at a time, and average the mean square displacement $\langle |\Delta \vec{r}|^2\rangle$ over the different realizations of the walk.

# In[ ]:


import numpy
import matplotlib.pyplot as plt 


# In[ ]:


# Number of steps
N = 100
# Number of walks
M = 1000
# Number of dimensions
dims = 3
# Size of step
delta = 1.0

# The initial position is the origin
position = numpy.zeros((M, dims))

# Random walk
msd = []
for i in range(N):
    for p in position:
        # Fixed displacement
        dr = delta * numpy.random.choice([-1, 1], size=dims)
        p += dr
    msd.append(numpy.sum(position**2) / M)

time = numpy.array(range(N))
plt.plot(time, msd, 'o', label='Data')
plt.plot(time, dims * delta**2 * time, '-', label='Theory')
plt.xlabel('t')
plt.ylabel('MSD')
plt.legend()


# **Exercise 1**: plot the trajectory $\vec{r}(t) = (x(t), y(t))$ of a single walk in 2d 

# **Exercise 2**: code the following two kinds of displacements
# 
# 1. discrete north-south-east-west displacement in 2d
# 2. continuous displacement uniformly distributed on a square of side $\delta$ in 2d
# 
# For each case, compare the numerical data to the theoretical prediction.

# **Exercise 3**: measure the probability density function (pdf) $p(x,t)$ for a random walk in 1d with a uniformly distributed displacement on the interval $[-\delta, \delta]$. Choose $10$ time units and compare to the numerical results to the theoretical prediction for a random walk in the continuum limit.
# 
# *Hint*: to compute the pdf, use the function `numpy.histogram()` with `density=True`. The function returns the pdf values and the bins edges. The get the midpoints of the bins, modify the array like this ```bins = 0.5 * (bins[1:] + bins[:-1])```
