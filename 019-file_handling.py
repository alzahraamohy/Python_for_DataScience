-- To open an exiting file we use this structure.
file = open ("file path\ file name","mode")
the mode can be : w >>> write, to write or create file and it removes the past data
                  r >>> read
                  a >>> appeand, do not remove the past data

# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()

# Type of file content, string or what
type(FileContent)

**It is very important that the file is closed in the end. This frees up resources and ensures consistency across different python versions.**
-- # Close file after finish
file1.close()

-- Using the with statement is better practice, it automatically closes the file even if the code encounters an exception.
The code will run everything in the indent block then close the file object.

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)


# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))

