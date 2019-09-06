#!/usr/bin/env python
# coding: utf-8

'''
Error propagation
Estimate the error of a function according to the errors of its vaiables
https://en.wikipedia.org/wiki/Propagation_of_uncertainty
'''

# In[1]

# Import

from sympy import (init_printing,
                   symbols,
                   Symbol,
                   Function,
                   Derivative,
                   sqrt,
                   log,
                   Eq,
                   latex)
from IPython.display import display, Math, Latex
from decimal import Decimal

init_printing(use_latex='png',
              latex_mode='equation*',
              forecolor='White')

# change forecolor to white if your backgrond is black

# In[4]:
def round_to_error(x, Dx):
    '''
    This function rounds Dx to 2 significant digits,
    rounds x to the same precision, and returns a string.
    '''
    Dx_str = str('%s' % float('%.2g' % Dx))
    x_str = str(Decimal(str(x)).quantize(Decimal(Dx_str)))
    result = r'$f = {} \pm {}$'.format(x_str, Dx_str)
    return result


# In[3]:

# Define variables
# F = Function('F')

f, x, b_s, b_0, b_x = symbols('f, x, \\beta_s, \\beta_0, \\beta_x')

Df = Symbol(r'\Delta f')
Dx = Symbol(r'\Delta x')
Db = Symbol(r'\Delta \beta')

variables = (x, b_s, b_0, b_x)
delta_dict = {x: Dx,
              b_s: Db,
              b_0: Db,
              b_x: Db}

# In[4]:

# Define a mathematical function $F(x, \beta_s, \beta_0, \beta_t)$ :

F = 1/x * log((b_0 - b_s) / (b_x - b_s))

display(Eq(f, F))

# In[5]:
'''
Calculate the partial derevitives of the function G
for each of its variables,
sum up the squares of the obtained derivatives:
'''

f_sum_squares = 0
F_sum_squares = 0

for variable in variables:
    display(Eq(Derivative(f, variable), Derivative(F, variable).doit()))
    f_sum_squares = (f_sum_squares
                     + (Derivative(f, variable))**2
                     * (delta_dict[variable])**2)
    F_sum_squares = (F_sum_squares
                     + (Derivative(F, variable))**2
                     * (delta_dict[variable])**2)

# In[6]:
# The square root of the sum is the estimated error of the function F

DF = sqrt(F_sum_squares)
Df_ = sqrt(f_sum_squares)

display(Eq(Df, Df_))
display(Eq(Df, DF.doit()))


# In[7]:

F_num = F.evalf(subs={x: 120,
                      b_0: 100,
                      b_s: 20,
                      b_x: 60})

DF_num = DF.doit().evalf(subs={x: 120,
                               Dx: 1,
                               b_0: 100,
                               b_s: 20,
                               b_x: 60,
                               Db: 0.1})

display(Math(r'f = ' + str(F_num)))
display(Math(r'\Delta f = ' + str(DF_num)))  

result = r'f = {} \pm {}'.format(F_num, DF_num)
display(Latex(round_to_error(F_num, DF_num)))
