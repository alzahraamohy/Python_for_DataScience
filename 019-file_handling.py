-- To open an exiting file we use this structure.
file = open ("file path\ file name","mode")
the mode can be : 1) r : Opens the file for reading only, Raises a "FileNotFoundError" if the file does not exist.
                  2) w : Opens the file for writing only, If the file exists, it erases its contents.
                          If the file does not exist, it creates a new file.
                  3) a : Opens the file for appending only, doesn't erase its contents.
                    
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

# Write line to file
exmp2 = '/Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")

#write and read
with open('/Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())


Let's copy the file **Example2.txt** to the file **Example3.txt**:
# Copy file to another

with open('/Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


or
#Another example to copy file
sh.copyfile( 'D:\\1\\1.txt', 'D:\\1\\00\\0.txt')
#copy directory
sh.copytree('D:\\1\\00' , 'D:\\1\\33')
#move file or directory
sh.move('D:\\1\\1.txt' , 'D:\\1\\33\\55.txt') 






