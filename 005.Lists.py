-- A list is a sequenced collection of different objects such as integers, strings, and even other lists as well.

-- To create a list, type the list within square brackets [ ]
    # Create a list
    L = ["Michael Jackson", 10.1,1982,"MJ",1]

-- We can use negative and regular indexing with a list , "as we did in tubles"

-- # List slicing
    L[3:5]    #['MJ', 1]

-- We can use the method extend to add new "elements" to the list
    L = [ "Michael Jackson", 10.2]
    L.extend(['pop', 10])      #['Michael Jackson', 10.2, 'pop', 10]

-- Another similar method is "append". If we apply append instead of extend, we add "one element' to the list
    L = [ "Michael Jackson", 10.2]
    L.append(['pop', 10])    #['Michael Jackson', 10.2, ['pop', 10]]

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
