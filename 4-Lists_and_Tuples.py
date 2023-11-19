-- Tubles are ordered lists , comma separated, can be float or int or string
  Ratings = ( 10 , 100 , 3 , 5 )

-- we can contain the all types in one tuble
  x = ('zahra' , 3.88 , 1 )

-- we can access all elements by :
  x [0]  #'zahra'
  x [2]  #1

-- we can access a range
  x[0:2] #'zahra' , 3.88 , 1 

-- we can combine tubles by ' + '

-- we can use len to indicate the length of the tuple

-- if we want to sort a tuple we can use sorted function
  new = sorted(x)
-- 
