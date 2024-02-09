-- A list is a sequenced collection of different objects such as integers, strings, and even other lists as well.
-- List is mutable
-- To create a list, type the list within square brackets [ ]
    # Create a list
    L = ["Michael Jackson", 10.1,1982,"MJ",1]
    L[len(L) - 1]  >>> will  retrieve the last element by reducing the index by 1
    output >>> 1
    L[-2] >>> "MJ"

-- We can use negative and regular indexing with a list , "as we did in tubles"
-- List slicing, the first index is inclusive, and the second is exclusive
    L[3:5]    >>> ['MJ', 1]
    L[:3]     >>> ["Michael Jackson", 10.1,1982]

-- We can use the method extend to add new "elements" to the list
    L = [ "Michael Jackson", 10.2]
    L.extend(['pop', 10])      #['Michael Jackson', 10.2, 'pop', 10]

-- len function will return the number of elements in the list.

-- Another similar method is "append". If we apply append instead of extend, we add "one element' to the list
    L = [ "Michael Jackson", 10.2]
    L.append(['pop', 10])    #['Michael Jackson', 10.2, ['pop', 10]]

-- Join is a string method that takes a list of strings as an argument, 
    and returns a string consisting of the list elements joined by a separator string.
    new_str = "\n".join(["fore", "aft", "starboard", "port"])
    print(new_str)

    output:
    fore
    aft
    starboard
    port    

    *Example2
    name = "-".join(["García", "O'Kelly", "Davis"])
    print(name)
    Output:

    García-O'Kelly-Davis

-- As lists are mutable, we can change them. For example, we can change the first element as follows:
    # Change the element based on the index
    A = ["disco", 10, 1.2]
    print('Before change:', A)
    A[0] = 'hard rock'
    print('After change:', A)    #After change: ['hard rock', 10, 1.2]

-- We can break a string to a list using "split"
    'hard rock'.split()    #['hard', 'rock']
    'A,B,C,D'.split(',')   #['A', 'B', 'C', 'D']

-- You can clone list **A** by using  the following syntax:
    A = ["hard rock", 10, 1.2]
    B = A
    B = A[:]
    B            #['banana', 10, 1.2]

-- We can also delete an element of a list using the del
    del(A[0])
    print('After change:', A)    #After change: [10, 1.2]

-- membership elements (in , not in)
    checks if the things in left side is in the right side or not.
    >>> 'this' in 'this is a string'
    True
    >>> 'in' in 'this is a string'
    True
    >>> 'isa' in 'this is a string'
    False
    >>> 5 not in [1, 2, 3, 4, 6]
    True
    >>> 5 in [1, 2, 3, 4, 6]
    False

-- we can modifiy on lists , but strings not, so list is mutable and strings not, but both are ordered.

-- Useful Functions for Lists I
    1. len() returns how many elements are in a list.
    2. max() returns the greatest element of the list.
       How the greatest element is determined depends on what type of objects are in the list.
    3. min() returns the smallest element in a list.
    4. sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged. 


    







