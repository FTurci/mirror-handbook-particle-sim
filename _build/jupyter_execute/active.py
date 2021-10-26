#!/usr/bin/env python
# coding: utf-8

# ## Active Brownian particles
# 
# We study the overdamped Brownian dynamics of a self-propelled ("active") particle driven by an internal force $F_0 \hat{n}(t)$, where $\hat{n}(t)$ is a unit vector.
# 
# The equations of motion for a 2d active Brownian particle in a bath at temperature $T$ are
# $$
# \xi \frac{d\vec{r}}{dt} = F_0 \hat{n}(t) + \vec{\theta}(t)
# $$
# $$
# \xi_R \frac{d\phi}{dt} = \theta_R(t)
# $$
# where $\hat{n} = (cos(\phi), sin(\phi))$ and $\vec{\theta}$ and $\theta_R$ are stochastic forces related to the friction coefficients $\xi$ and $\xi_R$ by the usual fluctuation-dissipation relations.
# 
# Analytical results for this model can be found in http://arxiv.org/abs/0906.3418, see also https://arxiv.org/abs/1005.1343.

# In[ ]:


import numpy
import matplotlib.pyplot as plt 


# In[ ]:


# Model parameters
npart = 1000
ndims = 3
xi = 1.0
xi_R = 1.0 
k = 0.5
T = 1.0
dt = 0.01
nsteps = int(3.0 / dt)

# DETERMINE THE AMPLITUDE OF THE STOCHASTIC FORCES HERE!
# ------------------------------------------------------

# Overdamped Brownian dynamics
positions = numpy.zeros((npart, ndims))
msd = []
for i in range(nsteps):
    # Store MSD
    msd.append(numpy.sum(positions**2) / npart)

    # Integration step
    for position in positions:
        # CODE THE STOCHASTIC FORCES HERE!
        # --------------------------------
        # noise = numpy.random.normal(0.0, width, ndims)

        # CODE THE ACTIVE INTERNAL FORCE HERE!
        # ------------------------------------
        # force = numpy.zeros(ndims)
        position += noise + force * dt / friction

time = numpy.array(range(nsteps)) * dt
# This is to plot an horizontal line at height y
# plt.axhline(y, xmin=time[0], xmax=time[-1])
plt.xlabel('t')
plt.legend()


# **Exercise**: *active Brownian particle in a 1d channel*
# 
# 1. Project the equations of motion along the $x$-axis and determine analytically $\langle \cos{\phi(t)}\rangle$ and $\langle x(t)\rangle$.
# 
# 2. Simulate an active Brownian particle confined in a 1d channel and compute the displacement $\langle x(t) - x(0)\rangle$. Compare the simulation results against the analytical ones for selected values of $D=k_BT/\xi$ and $D_R=k_B T/ \xi_R$. Choose $\phi(0)=0$. Which factor controls the approach to equilibrium?
# 
# 3. Compute numerically the mean square displacement $\langle |x(t) - x(0)|^2 \rangle$ and compare it to the analytical results given in the above references.
