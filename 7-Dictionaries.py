-- The Dictionaries are conainers like sets , as its not accept dupelcation but it has "Keys" and "Values"

-- Keys must be defined first and must be immutable and unique.

-- The values can be immutable, mutable and duplicates.

-- Each key and value pair is separated by a comma.

-- Sample dictionary D={'a':0,'b':1,'c':2}
    to find the value of key (a) we search by key
      D["a"]      #0

-- To Find the keys of the dictionary D
      D.keys()    #dict_keys(['a', 'b', 'c'])

-- To Find the values of the dictionary D
      D.values()    #dict_keys([1 , 2 , 3])

-- We can add a new entry to the dictionary as follow
      D['d']= 3

-- We can also delete as follow
      del(D['a'])    #It removes the key and the value

-- We can search if an element is in or not by
      'b' in D        #True
