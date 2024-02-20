First , how to import a library ?
we have many methods.

1)  import libraryname  #in this case we need to write the name every time when use it
  import math

# Now you need to use the library name 'math' every time you access its functions
print(math.sqrt(25))  # Output: 5.0

2) import libraryname as ln  #we need to write"ln" every time when use it
import math

# Now you need to use the library name 'math' every time you access its functions
print(math.sqrt(25))  # Output: 5.0

3) from libraryname import function #only import one function
from math import sqrt  # Only importing the 'sqrt' function from 'math'

# Now you can use the 'sqrt' function directly without specifying 'math.'
print(sqrt(25))  # Output: 5.0

4) from libraryname import * #use function directly
from math import *  # Imports all functions and variables from 'math'

# Now you can use all functions from 'math' directly without specifying 'math.'
print(sqrt(25))  # Output: 5.0



Now lets move on to Math library:
-- use the previous import methods whith math function
here are the math functions

import math as m
m.factorial(x)
m.exp(x)
m.log()
m.log(x,y)
m.log10(x)
m.sqrt(x)
m.degrees(x)     #to transform from degree to radians
m.radians(x)      #from radians to degree
m.sin(x)     m.cos(x)      m.tan(x)
m.asin(x)      m.acos(x)      m.atan(x)
m.sinh(x)      m.cosh(x)      m.tanh(x)
m.asinh(x)      m.acosh(x)      m.atanh(x)
m.pi       m.e        m.tau       m.inf
m.copysign(a,b)
m.ceil(x)      #Approximation to the Most High
m.floor(x)     #Rounding down
m.erf(x)        #Error value function
m.gamma(x)      #Gamma Function



