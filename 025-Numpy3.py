1) another method like reshape
>>> from  numpy import *
a = matrix('{} {} ; {} {}'.format(1,2,3,4))
#[[1 2]
#[3 4]]
b = matrix('{} {} {};{} {} {}'.format(1,2,3,4,5,6))
#[[1 2 3]
#[4 5 6]]

2) *trace* to sum diagonal numbers
>>> from  numpy import *
a =arange(9)
b = a.reshape(3,3)
c = trace(b)    #12

3) *linalg.det* to find determant, *linalg.eig* to find eign values
>>> from  numpy import *

a =arange(9)
b = a.reshape(3,3)
c = linalg.det(b)
d = linalg.eig(b)

4) values from a matrix
>>> from  numpy import *
a =arange(10) #[0 1 2 3 4 5 6 7 8 9]
c = a[3]    #3
d = a[3:9]  #[3 4 5 6 7 8]
e = a[3:9:2]  #[3 5 7]
f = a[-1]  #9
g = a[-3]  #7

**note** it is same for 2d matrix, but it will output rows not single elements

5)  if you want to differentiate between rows and columns and output single or many elements, use comma , 
>>> from  numpy import *
a =arange(36).reshape(6,6)
#[[ 0  1  2  3  4  5]
 #[ 6  7  8  9 10 11]
 #[12 13 14 15 16 17]
 #[18 19 20 21 22 23]
 #[24 25 26 27 28 29]
 #[30 31 32 33 34 35]]

c = a[3,1]    #19
d = a[3,:]    #[18 19 20 21 22 23]
e = a[:,2]    #[ 2  8 14 20 26 32]
f = a[:,1:3]     #[[ 1  2]
                  #[ 7  8]
                  #[13 14]
                  #[19 20]
                  #[25 26]
                  #[31 32]]
g = a[1:2,:]      #[[ 6  7  8  9 10 11]]


6) make a steps 
c = a[::2,::3]
d = a[::-1,::-1]
e = a[:2:-1,:3:-1]
f = a[2::2,3::3]
g = a[-1::,-1::]

7) change values
from  numpy import *
a =arange(16).reshape(4,4)
print(a)
a[2,3] = 0
print(a)
a[:,3] = 0 
print(a)
a[2,:] = 0 
print(a)
a[:,:] = 0 
print(a)

8) 
















