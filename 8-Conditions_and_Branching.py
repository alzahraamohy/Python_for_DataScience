-- Comparison operations compare some value or operand and based on a condition, produce a Boolean. When comparing two values you can use these operators:

    equal: (==)
    not equal: !=
    greater than: >
    less than: <
    greater than or equal to: >=
    less than or equal to: <=


-- a = 5
   a == 6      #The result is False, as 5 does not equal to 6.

   i = 6
   i > 5        #True

-- # Inequality Sign
   i = 2
   i != 6      #will outcomes True for all integers except 6.

   i = 6
   i != 6      #False

--  Equality sign can used to compare the strings
   "ACDC" == "Michael Jackson"      #False

   "ACDC" != "Michael Jackson"      #True

-- The inequality operation is also used to compare the letters/words/symbols according to the ASCII value of letters
      Note: Upper Case Letters have different ASCII code than Lower Case Letters,
      which means the comparison between the letters in Python is case-sensitive.
    # Compare characters
      'B' > 'A'
    # Compare characters
      'BA' > 'AB'

--  Branching allows us to run different statements for different inputs.
    It is helpful to think of an **if statement** as a locked room, if the statement is **True** we can enter the room 
    and your program will run some predefined tasks, but if the statement is **False** the program will ignore the task.

    1) # If statement example
      age = 19
    #expression that can be true or false
      if age > 18:
           print("you can enter" )
    #The statements after the if statement will run regardless if the condition is true or false 
      print("move on")

    #Then the output is 
                  you can enter
                  move on


    2) # Else statement example
       age = 18
       if age > 18:
            print("you can enter" )
       else:
            print("go see Meat Loaf" )
    
       print("move on")

    #Then the output is 
                  go see Meat Loaf
                  move on


    3) # Elif statment example
       age = 18
       if age > 18:
           print("you can enter" )
       elif age == 18:
           print("go see Pink Floyd")
       else:
           print("go see Meat Loaf" )
    
       print("move on")

    #Then the output is 
                  go see Pink Floyd
                  move on

-- Logical Operatpors:
    **and**  **or**  **not**
    The and statement is only True when both conditions are true. 
    The or statement is True if one condition, or both are True. 
    The not statement outputs the opposite truth value.

    1) #Example on and
    album_year = 1980
    if(album_year > 1979) and (album_year < 1990):
           print ("Album year was in between 1980 and 1989")
    print("")
    print("Do Stuff..")

    #Output
    Album year was in between 1980 and 1989

    Do Stuff..

    2) #Example on or
    album_year = 1990
    if(album_year < 1980) or (album_year > 1989):
           print ("Album was not made in the 1980's")
    else:
           print("The Album was made in the 1980's ")

    #Output
    Album was not made in the 1980's


    3) #Example on not
    album_year = 1983
    if not (album_year == 1984):
        print ("Album year is not 1984")

    #Solution
        Album year is not 1984




