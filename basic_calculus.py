#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import init_printing, symbols, Integral, Derivative, sin, exp, Eq
from IPython.display import display
init_printing(use_latex=True, latex_mode='equation*') 

x = symbols('x')


# In[2]:


int_x = Integral(sin(x)*exp(x), x)
display(Eq(int_x, int_x.doit()))

derv_x = Derivative(sin(x)*exp(x), x)
display(Eq(derv_x, derv_x.doit()))

