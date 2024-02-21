It is one of the most important libraries used in Python,
which is strongly used in mathematical operations and dealing with arrays

from  numpy import *
a = sin(30)
b = cos(30)
c = tan(30)

print(a , b , c)

1) Note that we deal with numbers in radians not degrees
and to solve this problem use:

import numpy as np
import math as m
a = np.sin(m.radians(30))
b = np.cos(m.radians(30))
c = np.tan(m.radians(30))
print(a)
print(b)
print(c)

or

from  numpy import *

a = sin(deg2rad(30))
b = cos(deg2rad(30))
c = tan(deg2rad(30))

print(a)
print(b)
print(c)


2)  Round    >>> generates the round of number
#ex
from  numpy import *

a = round(3.68528)
b = round(3.68528,1)
c = round(3.68528,2)
d = round(3.68528,3)
e = round(3.68528,4)

print(a)
print(b)
print(c)
print(d)
print(e)

#output >>> 
4
3.7
3.69
3.685
3.6853


3)  Ceil & floor
from  numpy import *

a = floor(3.68528)    #3.0
b = ceil(3.68528)      #4.0

print(a)
print(b)

4)  mod >>> module, or use %
   ,power
from  numpy import *

a = mod(20,7)    # 6
b = power(2,5)    # 32

print(a)
print(b)


**How to write a matrix?**

1) use array function

from  numpy import *
a = [2,3,6,5,4,7,8]
b = array(num)
print(a)
print(b)

-- and to specify 2d array use "a" as
a = [[1,2,3],[5,3,6],[9,6,5]]

2) 
