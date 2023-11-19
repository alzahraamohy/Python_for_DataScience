-- The string can be in single quotes or double ' "
"Zahra" 'Zahra'
-- Each element in string has index
zahra[0]    #z
zahra[1:3]  #ahr
zahra[::2]  #zha appear the element +2 in the whole str
zahra[:3:2]  #zh the same but only in the first 3 indexs

-- to know the length of string use len
len("zahra")   #5 , it also count spaces

-- we can combine the strings 
x = "zahra"
y = x + "can code"    #"zahra can code"

-- Tubles - by applying any operation on string 
3 * zahra    #"zahra zahra zahra"

-- backslash for escape sequences \ 
  \n : for newline
  \t : for tab
  \\ : print \
  or place r before the " in string to print any sympol directly

-- use .upper() to convert to uppercase
  b = a.upper()

-- to replace a word with another use .replace(first(what in the str),second(what we want to replace))
  b = a.replace('zahra', 'mona')

-- to find a substring use .find('substring')
  zahra.find('hra')    #2  the starting index

-- 





