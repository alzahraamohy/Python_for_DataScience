-- Tubles are containers of ( strings , floats, intgers )

-- we can contain the all types in one tuble
    x = ('zahra' , 3.88 , 1 )

-- Tubles represented by " ( ) ".
    # Create your first tuple
    tuple1 = ("disco",10,1.2 )

-- Each element of a tuple can be accessed via an index.
    x [0]  #'zahra'
    x [2]  #1
    # Print the variable on each index
    print(tuple1[0])  #'disco'
    print(tuple1[1])  #10
    print(tuple1[2])  #1.2

-- We can know the type of eah element by 
    # Print the type of value on each index
    print(type(tuple1[0]))      #<class 'str'>
    print(type(tuple1[1]))      #<class 'int'>
    print(type(tuple1[2]))      #<class 'float'>

-- We can also use negative indexing 
    tuple1[-1]    #1.2
    
-- We can concatenate or combine tuples by using the + sign
    tuple2 = tuple1 + ("hard rock", 10)   
    # ('disco', 10, 1.2, 'hard rock', 10)

-- We can slice tuples, obtaining new tuples with the corresponding elements
    tuple2[0:3]    #('disco', 10, 1.2)
    # Note : we said from 0 to 3, not form 0 to 2 , we add increase extra 1

-- we can access a range
  x[0:2] #'zahra' , 3.88 , 1 

-- we can combine tubles by ' + '

-- we can use len to indicate the length of the tuple

-- if we want to sort a tuple we can use sorted function
  new = sorted(x)
-- 
