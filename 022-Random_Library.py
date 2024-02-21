import random as rn

1)  rn.random()     >>> generates a random number between 0 and 1
#ex
a = rn.random()
print(a)

2)   rn.randint()      >>> generates a random integer between any range two numbers
#ex
a = rn.randint(1,20)
print(a)

3)   rn.uniform()    >>> generates a random number between any range two numbers
#ex
a = rn.uniform(1,20)
print(a)

4)   rn.randrange()    >>> generates a random integer between 0 and this integer
#ex
a = rn.randrange(150)
print(a)

5)  rn.randrange()  >>> Another use, that it gives a random integer from this range but from the steps indicated
#ex
a =rn.randrange(0,20,2)
print(a)
#output ex >> 2,4,6,8,10

6)  rn.choice()      >>> select a random element from this list or set 
#ex
a =rn.choice(['a','b','c'])    
print(a)
#ex output >>> a

#can be string also, will generate a random charachter
a =rn.choice('sweet home alabama')
print(a)
#output ex >>> w

7)  rn.sample()      >>> generates many numbers as you want, not only one
#ex
a =rn.sample(range(200) ,10)
print(a)
#ex output >>> [21, 72, 51, 94, 14, 145, 99, 111, 71, 7]

8)  rn.shuffle()        >>> Randomizes the list
#ex
items = [1,2,3,4,5,6]
rn.shuffle(items)
print (items)
#output    >>>   [1, 4, 6, 2, 3, 5]


