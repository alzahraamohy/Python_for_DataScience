1) lambda function, in one diemention
----> lambda is to make a non-named function in one line
>>> from numpy import *
#in this function will take the matrix "the matrix has only rows" for each number from 0 t0 9, cube it
x = fromfunction(lambda i: i**3, (10,))
print(x)    #[  0.   1.   8.  27.  64. 125. 216. 343. 512. 729.]

2) in two dimentions
>>> from numpy import *
x = fromfunction(lambda i,j: i+j, (4,5))
#i = 0 1 2 3
#j = 0 1 2 3 4
print(x)    #[[0. 1. 2. 3. 4.]
             #[1. 2. 3. 4. 5.]
            # [2. 3. 4. 5. 6.]
            # [3. 4. 5. 6. 7.]]
----> for each row, add it to j element to make a new columns equals i+j


3) or write in another way, in 1D
>>> from numpy import *
def powers(i):
    i = i**2
    return i
  
x = fromfunction(powers, (9,), dtype=int)
print(x)    #[ 0  1  4  9 16 25 36 49 64]
----------in 2D---------
>>> from numpy import *
def powers(i,j):
    i = i**j
    return i
  
x = fromfunction(powers, (4,5), dtype=int)
print(x)      #[[ 1  0  0  0  0]
             # [ 1  1  1  1  1]
            #  [ 1  2  4  8 16]
            #  [ 1  3  9 27 81]]

4) boolean function
>>> from numpy import *
m,n = 20, 5
def f(i):
    return (i % n == 0)
x = fromfunction(f, (m,), dtype=int)

print(x)    #[ True False False False False  True False False False False  True False
            #  False False False  True False False False False]


















