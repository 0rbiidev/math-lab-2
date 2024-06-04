Simple Partial Differential Equation solver programs exploring implicit and explicit methods implemented in Python. Written for University coursework to model the cooling over time of a 500C uniform aluminium rod with each end set to 0C. 

$\frac{\partial ^2 T(x,t)}{\partial x^2} = \frac{1}{k}\frac{\partial T(x,t)}{\partial t}$

## analytical.py

Implementation of the analytical solution. Used for reference and error calculation.

## implicitsolver.py

Uses the Implicit Crank-Nicholson Method of finite-difference PDE estimation.

## model.py

Implicit method using a non-uniform model of the bar's initial temperature.

## explicitsolver.py

Uses an explicit finite difference method. Central difference approximation is used for the second order derivitive and forward difference is used for the first order derivitive.
