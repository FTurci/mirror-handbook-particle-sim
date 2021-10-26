#!/usr/bin/env python
# coding: utf-8

# # Force-extension relation in DNA chains
# 
# We model the force-extension relation $f(\delta\ell)$ of a single polymer chain using the freely jointed chain (FJC) and worm-like chain (WLC) models and fit the theoretical results to experimental data for $\lambda$-DNA (from https://doi.org/10.1126/science.271.5257.1835).
# 
# Note: in this context, the WLC model is the continuous version of the Kratky-Porod model, which can be solved numerically. The FJC model is just the ideal chain model.

# In[ ]:


import numpy
from matplotlib import pyplot as plt

# Experimental data using the Brownian motion method
# From https://doi.org/10.1126/science.271.5257.1835
# Columns: Extension (um), Force (pN)
dna = numpy.loadtxt('data/dna_exp.txt', unpack=True)

# Exact solution of the worm-like chain model
# from https://doi.org/10.1016/S0006-3495(99)77207-3
# first column: <z> / L_0 (L_0 contour lenght)
# second column: F L_p / k_B (L_p persistence length) 
wlc = numpy.loadtxt('data/dna_wca.txt', unpack=True)

# Freely jointed chain
def L(x):
    """Langevin funcion"""
    def coth(x):
        return numpy.cosh(x) / numpy.sinh(x)
    return coth(x) - 1/x

plt.xlabel('Extension [um]')
plt.ylabel('Force [pN]')
plt.plot(dna[0], dna[1])
#plt.semilogy(dna[0], dna[1], 'o')
#plt.plot(wlc[0], wlc[1])


# **Excercice 1**: *$\lambda$-DNA*
# 
# Compare the force-extension experimental data for $\lambda$-DNA, provided in the above array `dna`, to the exact solution of the following two models:
# - the FJC model, as given in class. The Langevin function $L(x) = \coth(x) - 1/x$ is coded above for convenience 
# - the WLC model, as provided numerically in the `wlc` array above, which gives $F \ell_p / k_B$ as a function of $\delta\ell / L$ (see https://doi.org/10.1016/S0006-3495(99)77207-3).
# 
# For each model, adjust the parameters to best fit the experimental data. You can fit the data using one of the scipy functions mentioned in the `fit.ipynb` notebook or simply adjust the parameters by hand. Assume room temperature. From this analysis:
# 
# 1. estimate of the effective Kuhn segment $b$ using the FJC model
# 2. estimate of the persistence length $\ell_p$ and contour lenght $L$ using the WLC model.
# 
# **Exercice 2**: *one-dimensional ideal chain*
# 
# A simple (though unphysical) model, which can be treated analytically for long enough chains, is the one-dimensional ideal chain. Suppose the chain is composed by $N$ segments of length $a$, of which $M$ are oriented along the positive axis. The contour length is $L=Na$.
# 
# 1. Verifiy that the number of possible conformation with end-to-end distance $R$ is
# $$
# \Omega(R) = \frac{N!}{M!(N-M)!}
# $$
# and express $R$ in terms of $M$ and $N$.
# 2. Find the free energy $F(R)$ for fixed $R$
# 3. At constant $T$, the work done on the chain by an external force $\vec{f}$ is $\delta W = -\vec{f}\cdot d\vec{R} = dF$. Using the Stirling approximation, show that the force-extension relation can be written as 
# $$
# f = - \frac{\partial F}{\partial R} \approx \frac{k_B T}{2a} \log{\frac{1+\frac{R}{ML}}{1-\frac{R}{ML}}}
# $$
# 4. Discuss the limits $F\rightarrow 0$ and $F\rightarrow \infty$. 
# 5. To cross check, find the force-extension relation by calculating the partition function of the perturbed system with Hamiltonian $H=H_0 - fR$.
# 
# **Exercice 3**: *Gaussian chain model*
# 
# Determine the force-extension relation $f(\delta\ell)$ in a Gaussian chain of $M+1$ effective monomers interacting through the effective hamiltonian
# $$
# \mathcal{H}_0 = \sum_{i=1}^M \frac{3k_BT}{2b^2} |\vec{R}_{i+1} - \vec{R}_i|^2
# $$
# where $b$ is the Kuhn segment and $\vec{R}_i$ is the position of monomer $i$. Remember that the vectors $\vec{b}_i=\vec{R}_{i+1} - \vec{R}_i$ are independent variables.
# 
# **Exercice 4**: *Worm-like chain model*
# 
# We look for some limiting behavior of the worm-like chain (WLC) model. We consider $N+1$ monomers with bond length $a$.  In this model, the Hamiltonian contains the following bending energy term
# $$
# U_b = - \frac{B}{a^3} \sum_{i=1}^N \vec{a}_i\cdot\vec{a}_{i+1} = - \frac{B}{a} \sum_{i=1}^N \cos{\Theta_i}
# $$
# where $B$ is the bending modulus, $\vec{a}_i$ is the distance between monomer $i+1$ and $i$ and $\Theta_i$ is the corresponding angle. Note: this model is usually studied in its continuous version.
# 
# Write down the partition function and obtain approximate force-extension relations for (i) small forces ($f\rightarrow 0$) and (ii) large forces ($f\rightarrow \infty$). In case (i), which result is recovered?
# 
# 
# 
# 
# 
