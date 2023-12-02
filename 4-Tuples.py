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

-- We can obtain the length of a tuple using the length command
    len(tuple2)         #5

-- We can sort the values in a tuple and save it to a new tuple
    Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
    RatingsSorted = sorted(Ratings)
    RatingsSorted         #[0, 2, 5, 6, 6, 8, 9, 9, 10]

-- Nested Tuple

    A tuple can contain another tuple as well as other more complex data types. This process is called 'nesting'. 
    NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2))) 
    # Print element on each index, including nest indexes

    print("Element 2, 0 of Tuple: ",   NestedT[2][0])    #Element 2, 0 of Tuple:  pop
    print("Element 4, 1 of Tuple: ",   NestedT[4][1])    #Element 4, 1 of Tuple:  (1, 2)

    # Print the first element in the second nested tuples

    NestedT[2][1][0]    #'r'

    #  Print the second element in the second nested tuples

    NestedT[2][1][1]    #'o'
