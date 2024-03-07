1) to convert to a date format
>>> from numpy import *
x = array('2015-07-04', dtype=datetime64)    #2015-07-04
print(x)
or
x = datetime64('2015-07-04')      #2015-07-04

2) making an operations on dates , before and after that date
  ----> after date
>>> from numpy import *
x = datetime64('2015-07-04')
y = x + arange(12)    #remember that arange is like a matrix
print(x)    #2015-07-04
print(y)      #['2015-07-04' '2015-07-05' '2015-07-06' '2015-07-07' '2015-07-08'
             # '2015-07-09' '2015-07-10' '2015-07-11' '2015-07-12' '2015-07-13'
            #  '2015-07-14' '2015-07-15']

  -----> before date
>>> y = x - arange(12)
             #['2015-07-04' '2015-07-03' '2015-07-02' '2015-07-01' '2015-06-30'
            # '2015-06-29' '2015-06-28' '2015-06-27' '2015-06-26' '2015-06-25'
            # '2015-06-24' '2015-06-23']

3) The difference in days
>>> from numpy import *
x = datetime64('2015-07-04')
y = datetime64('2018-09-21')
z = y-x

print(z)    #1175 days


