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

5)  rn.randrange()  >>> another use, that it gives random integer from this range but from the steps indicated
#ex
a =rn.randrange(0,20,2)
print(a)
#output ex >> 2,4,6,8,10

6)  rn.choice()      >>> select random element from this list or set 
#ex
a =rn.choice(['a','b','c'])    #can be string also
print(a)
#ex output >>> a




