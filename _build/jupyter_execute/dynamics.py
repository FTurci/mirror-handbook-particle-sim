#!/usr/bin/env python
# coding: utf-8

# # Dynamic correlation functions
# 
# We will study the dynamics of a system composed of $N=8000$ particles under periodic boundary conditions and interacting via the Lennard-Jones potential
# $$
# u(r) = 4\epsilon \left[(\frac{\sigma}{r})^{12} - (\frac{\sigma}{r})^6\right]
# $$
# which provides a good description of the properties of nobel gases (Ar, Xe, Ne). 
# 
# We will analyze trajectories obtained from molecular dynamics simulations performed in the microcanonical ensemble, at a density $\rho=0.85$ and several temperatures. As usual, energies and lengths are measured in units of $\epsilon$ and $\sigma$, respectively. The following values provide a good description of the properties of Argon using the Lennard-Jones potential: $\epsilon\approx 120 K$ and $\sigma \approx 3.4\times 10^{-10}m$.

# We download the trajectory files (in compressed xyz format) and store them in the current directory. They are bigger than the ones we used to study the structure, so be patient

# In[ ]:


from atooms.core.utils import download

download('https://moodle2.units.it/pluginfile.php/367456/mod_folder/content/0/lammps-T0.7.xyz.gz', '.')
download('https://moodle2.units.it/pluginfile.php/367456/mod_folder/content/0/lammps-T4.0.xyz.gz', '.')


# Let us have a quick look at the thermodynamic state of the system

# In[ ]:


from atooms.trajectory import TrajectoryXYZ

with TrajectoryXYZ('lj_T4.0.xyz.gz') as th:
    system = th[0]
    print(system.report())


# We notice that the fluctuations of the (kinetic) temperature look a bit weird: the reason is that the times at which the frames have been stored are spaced exponentially in time. This is a trick to cover both short and long time scales without occupying too much disk space.

# In[ ]:


import matplotlib.pyplot as plt

# Plot kinetic temperature as a function of time
with TrajectoryXYZ('lj_T4.0.xyz.gz') as th:
    T = [system.temperature for system in th]
    plt.plot(th.times, T)


# Finally, let's use some `postprocessing` tools to compute some dynamic correlation functions and plot them

# In[ ]:


import atooms.postprocessing as pp

with TrajectoryXYZ('lj_T4.0.xyz.gz') as th:
    cf = pp.MeanSquareDisplacement(th)
    cf.compute()
    plt.plot(cf.grid, cf.value, '-o')
    
with TrajectoryXYZ('lj_T0.7.xyz.gz') as th:
    cf = pp.MeanSquareDisplacement(th)
    cf.compute()
    plt.plot(cf.grid, cf.value, '-o')


# In[ ]:


with TrajectoryXYZ('lj_T4.0.xyz.gz') as th:
    cf = pp.VelocityAutocorrelation(th, th.times[:20])
    cf.compute()
    plt.plot(cf.grid, cf.value / cf.value[0], '-o')
    
with TrajectoryXYZ('lj_T0.7.xyz.gz') as th:
    cf = pp.VelocityAutocorrelation(th, th.times[:20])
    cf.compute()
    plt.plot(cf.grid, cf.value / cf.value[0], '-o')


# In[ ]:


kvectors = list(range(1, 10))

# Note: cf.grid is a list containing the list of wave-vectors
# as first entry and the list of times as second entry 
# cf.value is now a list of the correlation functions at fixed k
with TrajectoryXYZ('lj_T4.0.xyz.gz') as th:
    cf = pp.SelfIntermediateScattering(th, kgrid=kvectors)
    cf.compute()
    # We plot the F_s(k,t) for k=7
    plt.plot(cf.grid[1], cf.value[kvectors.index(7)], '-o')
    
with TrajectoryXYZ('lj_T0.7.xyz.gz') as th:
    cf = pp.SelfIntermediateScattering(th, kgrid=kvectors)
    cf.compute()
    # We plot the F_s(k,t) for k=7
    plt.plot(cf.grid[1], cf.value[kvectors.index(7)], '-o')


# **Exercise 1**: *Gaussian approximation*
# 
# 1) Test the Gaussian approximation
# $$
# F_s(k,t) = \exp{\left(-\frac{1}{6} k^2 t\right)}
# $$
# by superposing the actual self intermediate scattering function to its approximation for selected values of the wave-vector $k$.
# 
# *Hint*: use a log scale of the time axis for better visualization.
# 
# 2) Repeat the test for the lowest acceptable wave-vector, which can be selected by asking for a negative wave-vector (ex. -1) in  `kgrid`
