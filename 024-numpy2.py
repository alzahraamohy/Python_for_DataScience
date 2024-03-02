**Matrixes**

-- suppose we have a matrix called "a".
1) to reshape this matrix to size 5x5
>>> b = reshape(a,(5,5))

2) to use "rand" with a specific matrix size, it can be 2d or 3d
>>> b = random.rand(3,5)

3) shuffle is to rearrange the set or matrix to a random shape, it affects on "b" itself
>>> b = [1,2,3,4,5,6,7,8,9]
    random.shuffle(b)
    print(b) #[3, 1, 9, 7, 8, 5, 6, 2, 4]

4) you can create a matrix of zeros or ones only
>>> b = zeros(5)
    c= ones(3)

5) identity matrix
>>> b = eye(5)

6) full, is to make a matrix of specific size all of specific number
>>> b = full((3,3),30)
#[[30 30 30]
# [30 30 30]
 #[30 30 30]]

7) making a diagonal matrix
>>> b = diag(array([1,2,3,4]))
#[[1 0 0 0]
# [0 2 0 0]
#[0 0 3 0]
#[0 0 0 4]]
>>> b = diag(array([1,2,3,4]), k=3)
 #[[0 0 0 1 0 0 0]
 #[0 0 0 0 2 0 0]
 #[0 0 0 0 0 3 0]
 #[0 0 0 0 0 0 4]
 #[0 0 0 0 0 0 0]
 #[0 0 0 0 0 0 0]
 #[0 0 0 0 0 0 0]]

8) count_nonzero(a)   >>> counts how many nonzero numbers in matrix "a"
  or specifiy a specific number to include larger or smaller than
>>> count_nonzero(a > 5)
  or make output by each column
>>> count_nonzero(a > 5, axis = 1)
    
7) any(), returns true or false depends on the operation inside parantethese for any number

8) all(), returns true or false depends on the operation inside parantethese for all numbers


9) in the following code example , we made a matrix and apply operation on the numbers
from numpy import *
a =random.randint(5,20, size=9).reshape(3,3)
b = a>10          #shows true or false in all indexs compared by this condition
c = a<15
d = a[b]          #shows the numbers that outputs "true" in "b"
e = a[c]
print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
>>> output
[[16 12 18]
 [19 10 11]
 [ 9 18  6]]
-------------------------
[[ True  True  True]
 [ True False  True]
 [False  True False]]
-------------------------
[[False  True False]
 [False  True  True]
 [ True False  True]]
-------------------------
[16 12 18 19 11 18]
-------------------------
[12 10 11  9  6]


10) isclose, is to show that the number in matrix 1 , is closed to number in matrix 2 in the same index
  under a condition called"rtol"
from  numpy import *
a =arange(9).reshape(3,3)
b =arange(9).reshape(3,3)
c = 2*b
d = isclose(a,b,rtol = 0.1)
e = isclose(a,c,rtol = 0.1)
print(a)
print('-------------------------')
print(b)
print('-------------------------')
print(c)
print('-------------------------')
print(d)
print('-------------------------')
print(e)
>>> output
[[0 1 2]
 [3 4 5]
 [6 7 8]]
-------------------------
[[0 1 2]
 [3 4 5]
 [6 7 8]]
-------------------------
[[ 0  2  4]
 [ 6  8 10]
 [12 14 16]]
-------------------------
[[ True  True  True]
 [ True  True  True]
 [ True  True  True]]
-------------------------
[[ True False False]
 [False False False]
 [False False False]]

11) to multpliy matrixes
from  numpy import * 
a =arange(5)
b =empty(5)
multiply(a, 10, out=b) #multpliy mat 1 by 10 and store the output in "b"

print(a)
print(b)
>>> output
[0 1 2 3 4]
[ 0. 10. 20. 30. 40.]

12) to make a matrix powered by a number 
from  numpy import *
a =arange(5)
b =empty(5)
power(a, 4, out=b)

print(a)
print(b)

13)  add.reduce is to sum all the matrix numbers
>>> from  numpy import *
a =arange(15)
b = add.reduce(a)
print(a)
print(b)
>>> output > 105


14) multiply.reduce make the same concept as add.reduce for multiplication

15) multiply.outer, multiples the outer number of the matrix
>>> from  numpy import *
a =arange(2,8)
b = multiply.outer(a,a)
print(a)
print(b)
>>> [2 3 4 5 6 7]
[[ 4  6  8 10 12 14]
 [ 6  9 12 15 18 21]
 [ 8 12 16 20 24 28]
 [10 15 20 25 30 35]
 [12 18 24 30 36 42]
 [14 21 28 35 42 49]]


16)   Add all the previous numbers
from  numpy import *
a =arange(10)
b = add.accumulate(a)
print(a)
print(b)

17) multiply.accumulate is the same concept

18) len in sets, returns the number of elements but returns the number of rows in the matrix
from  numpy import *
a =arange(12)
b = len(a)        #12
c = a.reshape(3,4)
d = len(c)    #3

-- to solve this confusion >>use *size* to always return number of elements in all dimensions


19)   shape returns the  dimensions
from  numpy import *
a =arange(12)
b = a.shape    #(12,)
c = a.reshape(3,4)
d = c.shape        #(3,4)

20) ndim returns how many dimensions
from  numpy import *
a =arange(12)
b = a.ndim    #1
c = a.reshape(3,4)
d = c.ndim    #2

21) dtype returns the type of data 
from  numpy import *
 
a =array(['a','d','g','h','j'])
b = a.dtype    #<U1

c = arange(12)
d = c.reshape(3,4)
e = d.dtype    #int32








