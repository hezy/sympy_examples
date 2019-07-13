# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:43:31 2019

@author: hezya
"""

#from sympy import *
from sympy import init_printing, symbols, Derivative, sqrt, log, Eq
from IPython.display import display
init_printing(use_latex=True, latex_mode='equation*', forecolor='White') 
#remove "White" if your background is white
 
g, Delta_g, t, theta_s, theta_0, theta_t, Delta_t, Delta_theta = symbols ('g, Delta_g, t, theta_s, theta_0, theta_t, Delta_t, Delta_theta')

variables = (t, theta_s, theta_0, theta_t)

deltadict =	{
        t: Delta_t,
        theta_s: Delta_theta,
        theta_0: Delta_theta,
        theta_t: Delta_theta}

def G(*variables):
    return 1/t * log( (theta_0 - theta_s) / (theta_t - theta_s) )

display(Eq(g, G(*variables)))

g_sum_squares = 0
G_sum_squares = 0

for variable in variables:
    g_derivative = Derivative(g,variable) 
    G_derivative = Derivative(G(*variables), variable)
    display(Eq(g_derivative, G_derivative.doit()))
    g_sum_squares = g_sum_squares + (g_derivative * deltadict[variable])**2
    G_sum_squares = G_sum_squares + (G_derivative * deltadict[variable])**2
    

Delta_G = sqrt (G_sum_squares)
Delta_g_ = sqrt (g_sum_squares)

display(Eq(Delta_g,Delta_g_))
display(Eq(Delta_g,Delta_G.doit()))


