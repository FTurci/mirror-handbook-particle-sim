#!/usr/bin/env python
# coding: utf-8

# ## Least-square fits with python 
# 
# There are several ways to perform least-square fits in python. Here are a few:
# 
# 1. [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html) for simple linear regression
# 2. [numpy.polfyit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html) for simple polynominal fits
# 3. [scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) for arbitrary fitting functions
# 4. [lmfit](https://lmfit.github.io/lmfit-py/) if you really need to get full control over fit parameters
# 
# In this simple notebook, we use the function `curve_fit()` defined in `scipy.optimize`. Here is how it works to fit an exponential with noise.

# In[ ]:


import numpy
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * numpy.exp(-b * x) + c
xdata = numpy.linspace(0, 4, 50)

y = func(xdata, 2.5, 1.3, 0.5)
numpy.random.seed(1729)
y_noise = 0.2 * numpy.random.normal(size=xdata.size)
ydata = y + y_noise


# Here is the fit. The optimized parameters are stored in the `popt` array returned by the function 

# In[ ]:


plt.plot(xdata, ydata, 'o', label='data')
popt, pcov = curve_fit(func, xdata, ydata)
# Note the *popt syntax unpacks the array into individual variables
plt.plot(xdata, func(xdata, *popt), '-')


# **Exercise:**
# 
# With strongly varying functions, like an exponential, is better to linearize the data and do a simple linear fit. Try fitting the linearized data and extract `a`, `b`. 

# ## Fitting the liquid-gas phase coexistence curve
# 
# The data below show the liquid-gas coexistence pressure P(T) as a function of temperature for water (also known as saturation pressure).
# 
# Source: NIST (National Institute of Standards and Technology)

# In[ ]:


import numpy
from matplotlib import pyplot as plt

T, P = numpy.loadtxt('data/coexistence_water_vapor.txt', unpack=True)
plt.ylabel('P [MPa]')
plt.xlabel('T [K]')
plt.plot(T, P, 'o')


# **Exercise**: *Clausius-Clapeyron equation*
#  
# To determine the coexistence pressure $P(T)$ we will use the Clausius-Clapeyron equation
# $$
# \frac{dP}{dT} = \frac{L}{T(v_g - v_l)}
# $$
# where $L$ is the molar latent heat of vaporisation, $v_g$ is the molar volume of the gas, $v_l$ is the molar volume of the liquid. 
# 
# 1. Find an analytical expression for the coexistence curve $P(T)$ under the following assumptions: the vapor is an ideal gas, the liquid is incompressible with $v_l<<v_g$, $L$ is constant.
# 2. Fit the experimental data to the functional form found above and determine the molar latent heat $L$. (Do it in a *clever* way!)
