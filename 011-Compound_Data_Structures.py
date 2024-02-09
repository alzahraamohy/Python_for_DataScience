-- We can include containers in other containers to create compound data structures.
For example, this dictionary maps keys to values that are also dictionaries!

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
We can access elements in this nested dictionary like this.
 >>> helium = elements["helium"]  # get the helium dictionary
 >>> hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
 >>> oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
     elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
     print('elements = ', elements)

The output will be:
 >>> elements =  {"hydrogen": {"number": 1,
                          "weight": 1.00794,
                          "symbol": 'H'},
                  "helium": {"number": 2,
                          "weight": 4.002602,
                          "symbol": "He"}, 
                  "oxygen": {"number": 8, 
                          "weight": 15.999, 
                          "symbol": "O"}}


**Additional example**

student_records = {
    'John': {
        'age': 20,
        'major': 'Computer Science',
        'grades': [85, 90, 92]
    },
    'Emma': {
        'age': 19,
        'major': 'Mathematics',
        'grades': [95, 88, 91]
    }
}

>>> Adding a new student:

        student_records['Alex'] = {
              'age': 21,
              'major': 'Physics',
              'grades': [80, 85, 88]
                }

>>> Adding a grade for an existing student:

        student_records['John']['grades'].append(88)


