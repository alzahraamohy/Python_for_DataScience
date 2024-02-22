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

-- or use range to make a matrix
a = array([range(i, i + 3) for i in [2, 4, 6]])
#output 
[[2 3 4]
 [4 5 6]
 [6 7 8]]

2) Variables can be defined after writing them
from  numpy import *
a = array([('x',3,4.2),('y',4,5.3),('z',5,6.3)],
           dtype =[('name','U5'),('number','i2'),      #U5, is a string from 5 characters
                   ('value','f4')])
print(a)

3)   To make an empty matrix  
a = empty((3,2))
print(a)

4)   
a = random.uniform(1,10)   #Gives random number from 1 to 10
b = random.uniform(1,10,20)   #Gives random 20 numbers from 1 to 10
-- Note that "random" is a function in Numpy library

5)   matrix of random numbers between 0 and 1, of size 2x3
a =random.random((2,3))

6)   random.normal  # Generate an array of 10 random numbers sampled from a normal distribution
from  numpy import *
a =random.normal(0,1,10)
print(a)

7)    random.randint   
-- a =  random.randint(150)   #generates random integer from 1 to 150
-- a =random.randint(5, size=7)   #generates 7 random integers in range from 1 to 5
-- a =random.randint(5,20, size=7)   ##generates 7 random integers in range from 5 to 20
-- a = random.randint(0, 10, (3, 3))   #generates a 2d matrix from random integers from 0 to 10
-- a = random.randint(5,10, size=(3, 4, 5))   ##generates a 3d matrix from random integers from 5 to 10

8)   reshape
a = random.randint(1,60,25)
b = reshape(a,(5,5))   #reshape the list to a 5x5 matrix






