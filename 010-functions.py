-- Welcome to this lesson on Functions! Functions are useful blocks of code that allow you to encapsulate a task.

**How to write a function**
  def function_name(arguments):    #header
      operations                  #body
    return 

-- And note that we can make a function without arguments, in this case, we do not use return.
    we use functions in the body like print.
-- Function names follow the same naming conventions as variables.

      
-- Example of a function definition:

    def cylinder_volume(height, radius):
        pi = 3.14159
    return height  *pi*  radius ** 2

  After defining the cylinder_volume function, we can call the function like this.

    cylinder_volume(10, 3)


    
--We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

    def cylinder_volume(height, radius=5):
        pi = 3.14159
    return height  *pi*  radius ** 2

When call it
cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name



**Variable Scope**
  If a variable is created inside a function, it can only be used within that function.
  Accessing it outside that function is not possible.
  
    ## This will result in an error
    def some_function():
        word = "hello"      #local variable
 
    print(word)

    ## This works fine
    word = "hello"      #Global variable

    def some_function():
    print(word)


**Documentation**
  Docstrings are a type of comment used to explain the purpose of a function, and how it should be used.
-- We write like a comment to explain input & output or anything else in the function body between triple double quotes """ """.

def population_density(population, land_area):
    """ Calculate the population density of an area.
    INPUT:
    OUTPUT: 
    """
    return population / land_area


**Lambda Expressions**
  lambda expressions to create anonymous functions. That is, functions that don’t have a name.
  syntax:
  >>> lambda parameters: expression

  With a lambda expression, this function:

  def multiply(x, y):
      return x * y
    
  can be reduced to:

  multiply = lambda x, y: x * y

>> We can call multiply like this:
  multiply(4, 7)


-- A get method is for obtaining an attribute value. A set method is for changing an attribute value.
    If you were writing a Shirt class, the code could look like this:

class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price
  
----> If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
      
