we use a function inside numpy library called " polynomial" 

1) making a best-fit line
>>> import numpy as np
Polynomial = np.polynomial.Polynomial

X= np.array([0,20,40,60,80,100,120,140,160,180])
Y= np.array([10,9,8,7,6,5,4,3,2,1])

points,stats = Polynomial.fit(X,Y,1,full=True)
print(points)    #5.5 - 4.5 x

---> Polynomial with capital P, is a variable, but with small p is the function to call
---> we assigned x-axis and y-axis by the *same number* of elements by using set of array
---> points > is a varible stores the output of calling *fit* function for Polynomial
    --> the fit function first attribute shows the relation between X and Y 
    --> second attribute *1* says that the relation is from the first degree
    --> full=True > means that the relation is between all points.
--> the output 5.5 - 4.5 x
** remember** Y = M X + C    Straight-line equation
    --> 5.5 is the slope
    --> -4.5 is C value, Point of intersection with y-axis

2) how to generate equations?
-- the number of elements you enter, decides the degree of the equation
>>> from numpy import *
#poly1d is a function
a = poly1d((-7))    #-7
b = poly1d((-7,2))    #-7 x + 2
c = poly1d((-7,2,1))    #-7 x^2 + 2 x + 1
d = poly1d((-7,2,1,3))    #-7 x^3 + 2 x^2 + 1 x + 3
e = poly1d((-7,2,1,3,6))    #-7 x^4 + 2 x^3 + 1 x^2 + 3 x + 6

3) You can also substitute it into the equation
>>> from numpy import *
a = poly1d((-7,2,1,3,6))
b=a(5)    #-4079


4) you can make a direct substitution and make an equation in the same line
>>> from numpy import *
a = polyval((1,2),2)
print(a)    #4
---> (1,2) is the equation
---> 2 is the value to substitute

5) Derivation of the equation by polyder 
>>> from numpy import *
a =polyder(poly1d((1,2,3)))
b =polyder(poly1d((1,2,3)),2)

print(a)  #2 x + 2
print(b)  #2
print(a(2))    #for substitution

---> if you only wrote an equation without outside number,The equation will be derived once
---> if you wrote a number, The equation will be derived times of this number

6) Integration of the equation **same use explanation as derivative**
>>> from numpy import *

a =polyint(poly1d((1,2,3)))    #0.3333 x^3 + 1 x^2 + 3 x
b =polyint(poly1d((1,2,3)),2)    #0.08333 x^4 + 0.3333 x^3 + 1.5 x^2

print(a(2))    #for substitution
**note** Python ignores the constant in integration.

7) Roots of the equation (solution to the equation, the numbers that make the equation equals zero)
---> depends of the degree of the equation, the number of solutions will generate
---> ex: thrid degree >> three solutions
  
>>> from numpy import *
a =roots(poly1d((1,2)))
b =roots(poly1d((1,2,3)))
print(a)    #[-2.]
print(b)      #[-1.+1.41421356j -1.-1.41421356j]








