**If Statement**
  runs or skips code based on whether a condition is true or false. Here's a simple example.

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10

---------------------------
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':        #elif used to represent another condition
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:                            #else , in the case of no condition is true
    print('unrecognized season')
----------------------

-- Note that if you want to execute more than one line inside the if statement, use blocks { } from start to end.

**Complex Boolean Expressions**
-- Is the include logical and mathematical expressions inside the condition.
  For really complicated conditions you might need to combine some ands, ors and nots together.
  
  if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")
  if is_raining and is_sunny:
    print("Is there a rainbow?")
  if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
------------------------
** For loop**
A for loop is used to "iterate", or do something repeatedly, over an iterable.
  syntax example:
>>> cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
      for city in cities:
      print(city)
      print("Done!")
>>> output:
      new york city
      mountain view
      chicago
      los angeles
      Done!

-- range() is a built-in function used to create an iterable sequence of numbers    #range(start=0, stop, step=1)
  for i in range(3):
    print("Hello!")
 >>> Output:
    Hello!
    Hello!
    Hello!

-- Example 2
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    cities[index] = cities[index].title()
print(cities)

>>>Output
['New York City', 'Mountain View', 'Chicago', 'Los Angeles']


-- Example 3
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)
>>> Output:
['joey_tribbiani', 'monica_geller', 'chandler_bing', 'phoebe_buffay']
---------------
**While Loops**
  syntax:
  while condition:
    operation

--Ex1
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

## adds the last element of the card_deck list to the hand list
## until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())


**For Loops Vs. While Loops**
-- for loops are ideal when the number of iterations is known or finite.
-- while loops are ideal when the iterations need to continue until a condition is met.

----------------------------
**Break, Continue**  
-- break terminates a loop
-- continue skips one iteration of a loop
Used in for, while loops when we don't want a specific operation to happen inside the loop.

----------------------------
**Zip and Enumerate**
-- zip returns an iterator that combines multiple iterables into one sequence of tuples.
   Each tuple contains the elements in that position from all the iterables. For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) 
  >>> would output [('a', 1), ('b', 2), ('c', 3)]

-- In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)

-- enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. 
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
This code would output:

0 a
1 b
2 c
3 d
4 e

-------------------------
**List Comprehensions**
 you can create lists really quickly and concisely with list comprehensions. This example from earlier:

capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
  
can be reduced to:
capitalized_cities = [city.title() for city in cities]
  
>>> you can also include condition
squares = [x**2 for x in range(9) if x % 2 == 0]

-----------------------




































