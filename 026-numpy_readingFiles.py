-- Note, be careful when writing the path, especially when using slash
make it double slash \\

-- Consider this data, upload it to a text file and copy path
# Student data collected on 17 July 2014
# Researcher: Dr Wicks, University College Newbury

# The following data relate to N = 20 students. It
# has been totally made up and so therefore is 100%
# anonymous.

Subject Sex    DOB      Height  Weight       BP     VO2max
(ID)    M/F  dd/mm/yy     m       kg        mmHg  mL.kg-1.min-1
JW-1     M    19/12/95    1.82     92.4    119/76   39.3
JW-2     M    11/1/96     1.77     80.9    114/73   35.5
JW-3     F    2/10/95     1.68     69.7    124/79   29.1
JW-6     M    6/7/95      1.72     75.5    110/60   45.5
# JW-7    F    28/3/96     1.66     72.4    101/68   -
JW-9     F    11/12/95    1.78     82.1    115/75   32.3
JW-10    F    7/4/96      1.60     -       -/-      30.1
JW-11    M    22/8/95     1.72     77.2    97/63    48.8
JW-12    M    23/5/96     1.83     88.9    105/70   37.7
JW-14    F    12/1/96     1.56     56.3    108/72   26.0
JW-15    F    1/6/96      1.64     65.0    99/67    35.7
JW-16    M    10/9/95     1.63     73.0    131/84   29.9
JW-17    M    17/2/96     1.67     89.8    101/76   40.2
JW-18    M    31/7/96     1.66     75.1    -/-      -
JW-19    F    30/10/95    1.59     67.3    103/69   33.5
JW-22    F    9/3/96      1.70     -       119/80   30.9
JW-23    M    15/5/95     1.97     89.2    124/82   -
JW-24    F    1/12/95     1.66     63.8    100/78   -
JW-25    F    25/10/95    1.63     64.4    -/-      28.0
JW-26    M    17/4/96     1.69     -       121/82   39.


1) loading this data
from numpy import *
fname = 'C:\\Users\\DELL\\Desktop\\Python\\xx.txt'
dtype1 = dtype([('gender', '|S1'), ('height', 'f8')])
a = loadtxt(fname, dtype=dtype1, skiprows=9, usecols=(1,3)) 
print(a)

#output

[(b'M', 1.82) (b'M', 1.77) (b'F', 1.68) (b'M', 1.72) (b'F', 1.78)
 (b'F', 1.6 ) (b'M', 1.72) (b'M', 1.83) (b'F', 1.56) (b'F', 1.64)
 (b'M', 1.63) (b'M', 1.67) (b'M', 1.66) (b'F', 1.59) (b'F', 1.7 )
 (b'M', 1.97) (b'F', 1.66) (b'F', 1.63) (b'M', 1.69)]

---> fname is a variable that stores the path of the text file
---> dtype1 is a varible to declare which data type we are dealing with
---> loadtxt is the function to call the data with these properties
      --> data stored in fname
      --> data types declared in dtype1
      --> to skip first 9 rows, and only show the 1,3 columns

2) another method
  consider this data
    Median age at First Marriage, 1890-2010
Source: U.S. Bureau of the Census, www.census.gov
Year     Men      Women
1890     26.1     22.0
1900     25.9     21.9
1910     25.1     21.6
1920     24.6     21.2
1930     24.3     21.3

>>> from numpy import *
a,b,c = loadtxt('C:\\Users\\DELL\\Desktop\\Python\\xx.txt', unpack=True,skiprows=3)
print(a)
print(b)
print(c)

---> unpack is to make it unpackaged
#output
[1890. 1900. 1910. 1920. 1930.]
[26.1 25.9 25.1 24.6 24.3]
[22.  21.9 21.6 21.2 21.3]




