-- The string can be in single quotes or double ' "
  "Zahra" 'Zahra'
-- Each element in the string has an index
  zahra[0]    #z
  zahra[1:3]  #ahr
  zahra[::2]  #zha appears the element +2 in the whole str
  zahra[:3:2]  #zh the same but only in the first 3 indexes

-- to know the length of the string use len
  len("zahra")   #5 , it also count spaces

-- strings are immutable
     >>> greeting = "Hello there"
     >>> greeting = "Mello there"
     That second line in Python actually creates a new place in memory where the string greeting is stored,
     effectively creating a new string, a new object, even though it has the same name.

-- we can combine the strings 
  x = "zahra"
  y = x + "can code"    #"zahra can code"

-- Tubles - by applying any operation on the string 
  3 * zahra    #"zahra zahra zahra"

-- backslash for escape sequences \ 
  \n : for newline
  \t : for tab
  \\ : print \
  or place r before the " in the string to print any symbol directly


**Methods**
  
-- use .upper() to convert to uppercase
  b = a.upper()

-- to replace a word with another use .replace(first(what in the str),second(what we want to replace))
  b = a.replace('zahra', 'mona')

-- to find a substring use .find('substring')
  zahra.find('hra')    #2  the starting index

-- use .title() to capitalize every word in a string
    print("zahra mohy" .title()) >>>>> Zahra Mohy

-- use .islower() to check that the all text is lowercase
-- use .count() to count how many words repeat in the string
-- use .find() to find any character or string or word


**An important string method: format()**
-- Example 1 python print("Mohammed has {} balloons".format(27))
-- Example 1 Output >>>  Mohammed has 27 balloons

-- Example 2 python animal = "dog" action = "bite" print("Does your {} {}?".format(animal, action))
-- Example 2 Output >>> Does your dog bite?

**F-String Formatting**
Unlike the traditional methods (as shown above) where you need to use placeholders like %s and %d or the format() function,
F-strings provide a concise and convenient way to embed expressions inside string literals, using curly brackets {}.
The expressions will be replaced with their values when the string is evaluated.


--Example 1 - Using a Single Variable
name = "John"
print(f"Hello, {name}")
-- Example 1 Output >>> Hello, John

-- Example 2
a = 5
b = 3
print(f"The sum of {a} and {b} is {a+b}")
--Example 2 Output >>> The sum of 5 and 3 is 8


**Split Method**
-- A basic split method
new_str = "The cow jumped over the moon."
new_str.split()
Output is:
['The', 'cow', 'jumped', 'over', 'the', 'moon.']

-- The separator is space, and the maxsplit argument is set to 3
new_str.split(' ', 3)
Output is:
['The', 'cow', 'jumped', 'over the moon.']

-- Using '.' or period as a separator
new_str.split('.')
Output is:
['The cow jumped over the moon', '']

-- Using no separators but having a maxsplit argument of 3
new_str.split(None, 3)
Output is:
['The', 'cow', 'jumped', 'over the moon.']
