#!/usr/bin/env python
# coding: utf-8

# ## Jupyter notebook: first ride
# 
# To run a code cell, use `Ctrl-Enter` or click on `Run` in the toolbar.
# To edit a text cell, double click on it.
# 
# To plot a functions and data we use matplotlib, which works on lists and numpy arrays. Here we trace $y=x^2$

# In[1]:


import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(0.0, 6.0)
plt.plot(x, x**2, '-o')  


# We can superpose several curves

# In[2]:


y = 5 + 0.5 * x**2 
plt.plot(x, x**2, label='x^2')
plt.plot(x, y, label='y')
plt.xlabel('x')
plt.legend()


# Two hints :
# 
# - use the `Tab` key to complete variable and function names
# - add a question mark right after the name of a function and run the cell to show the corresponding help page

# In[ ]:


get_ipython().run_line_magic('pinfo', 'plt.plot')


# **Exercises** :
# 
# - add a code cell and plot $y=log(x)$ between 0.5 and 0.1
# - add a text cell using "Markdown" in the toolbar and add some text (you can write equations using latex syntax). Then enter `Ctrl-Enter` to render the text 
