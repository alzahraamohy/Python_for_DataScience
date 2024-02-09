--if we have 45 + 5 + 2 + 1 , then we call the numbers "operands" and the addictive symbol "operator"
--python can do different math operations ( + , - , * , /) and so on.. , "//" is for integer division ex: 25//6 = 4 but 25/6 = 4.166
-- Use ** for exponential >>> 3 ** 2 = 9
-- use ^ for bitwise xor
--python follows the mathematical conventions (precedence), like multiplying before adding and so on..
      The precedence as follow:
            1. Parentheses
            2. Exponentiation
            3. Multiplication and Division
            4. Addition and Subtraction
  
--when we assign a value to a variable A we use "=" operator and we can change it anytime and apply operations
  A = 5
  y = 2 * 5
  y = A / 2

-- # Check the Python Version
import sys
print(sys.version)

# Print string and error to see the running order
print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")
#The third print statement is not executed because the second line contains an error. 

# System settings about float type
sys.float_info
