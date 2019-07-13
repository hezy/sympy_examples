# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 01:16:01 2019

@author: hezya
"""

from sympy import init_printing, Symbol, symbols
from IPython.display import display

init_printing(use_latex=True, latex_mode='equation*', forecolor='White') 

delta__y, delta_a = symbols('Delta__y, delta_a')
deltax = Symbol("\Delta x")

print(printing.latex(delta__y))

display(delta__y)
display(deltax)