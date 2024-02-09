-- The Dictionaries are containers like sets, as it's not accept duplication but it has "Keys" and "Values"
-- Dictionaries are mutable, but their keys need to be any immutable type,like strings, integers, or tuples.
{key1:value1, key2:value2, key3:value3, key4:value4, ...}

-- Keys must be defined first and must be immutable and unique.

-- The values can be immutable, mutable and duplicates.

-- Each key and value pair is separated by a comma.

-- Sample dictionary D={'a':0,'b':1,'c':2}
    to find the value of key (a) we search by key
      D["a"]      #0
        print(D) >>> {'a':0,'b':1,'c':2}
        print(D.get("f"))    >>>> none     #get will return none, because "f" has no key here
        print(D.get("a"))    >>>>  0

-- To Find the keys of the dictionary D
      D.keys()    #dict_keys(['a', 'b', 'c'])

-- To Find the values of the dictionary D
      D.values()    #dict_keys([1 , 2 , 3])

-- We can add a new entry to the dictionary as follows
      D['d']= 3

-- We can also delete as follow
      del(D['a'])    #It removes the key and the value

-- We can search if an element is in or not by
      'b' in D        #True
-- we can use Identity Operators (is , is not) for boolean results
    The is operator checks whether two variables reference the same object in memory.

**important example**
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

the output is 
True
True
True
False  #Although the contents of a and c are the same, they refer to different list objects in memory.

-- 
