# -*- coding: utf-8 -*-
"""
Created on Mon May 27 13:51:14 2019

@author: hezya
"""

from sympy import *
from IPython.display import display, Math

init_printing(use_unicode=False, wrap_line=False, no_global=True)

x, gamma = symbols('x gamma')

L = 1/(gamma**2 + x**2)

i = Integral(L, (x, -oo, oo))
ii = integrate(L, (x, -oo, oo)) 

display(i)
display(ii)
